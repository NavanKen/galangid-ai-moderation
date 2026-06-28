import json
import logging

from google.genai import types
from pydantic import BaseModel, ValidationError
from typing import TypeVar
from pydantic import BaseModel
from app.config.config import settings
from app.config.exceptions import GeminiException, GeminiResponseError
from app.config.gemini import client

T = TypeVar("T", bound=BaseModel)
logger = logging.getLogger(__name__)


class BaseAIService:

    async def _call_gemini(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: type[T],
        temperature: float = 0.3,
    ) -> T:
        try:
            response = await client.aio.models.generate_content(
                model=settings.GEMINI_MODEL,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    response_mime_type="application/json",
                    temperature=temperature,
                ),
            )
        except Exception as e:
            logger.error("Gemini API Call fauled : %s", e)
            raise GeminiException(f"Gagal menghubungi Gemini AI: {e}")
        
        result_text = response.text
        if not result_text:
            logger.error("Gemini returned empty response")
            raise GeminiResponseError("Gemini mengembalikan response kosong")
        
        try:
            result_data = json.loads(result_text)
        except json.JSONDecodeError as e:
            logger.error("Failed to parse Gemini response as JSON: %s", e)
            raise GeminiResponseError(
                f"Response Gemini bukan JSON yang valid: {e}"
            )
        
        try:
            return response_model(**result_data)
        except ValidationError as e:
            logger.error("Gemini response doesnt match schema: %s", e)
            raise GeminiResponseError(
                f"Response Gemini tidak sesuai format yang diharapakan: {e}"
            )