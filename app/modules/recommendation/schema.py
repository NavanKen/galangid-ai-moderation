from pydantic import BaseModel, Field

class RecommendationRequest(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        description="Judul campaign",
    )
    description: str = Field(
        ...,
        min_length=1,
        description="Deskripsi lengkap campaign",
    )
    goal_amount: int | None = Field(
        default=None,
        gt=0,
        description="Target donasi dalam Rupiah",
    )
    category: str | None = Field(
        default=None,
        description="Kategori campaign",
    )


class Suggestion(BaseModel):
    aspect: str = Field(
        ...,
        description="Aspek yang disarankan: 'judul', 'deskripsi', 'transparansi', 'kredibilitas', 'kelengkapan'",
    )
    suggestion: str = Field(
        ...,
        description="Saran spesifik yang actionable",
    )
    priority: str = Field(
        ...,
        description="Prioritas: 'high', 'medium', 'low'",
    )
    example: str = Field(
        default="",
        description="Contoh konkret penerapan saran (opsional)",
    )


class RecommendationResponse(BaseModel):
    quality_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Skor kualitas campaign (0-100)",
    )
    strengths: list[str] = Field(
        default_factory=list,
        description="1-3 hal yang sudah baik dari campaign",
    )
    weaknesses: list[str] = Field(
        default_factory=list,
        description="1-3 kelemahan utama campaign",
    )
    suggestions: list[Suggestion] = Field(
        default_factory=list,
        description="Saran perbaikan (maks 5), urut dari prioritas tertinggi",
    )
    overall_feedback: str = Field(
        ...,
        description="Feedback keseluruhan yang ramah dan supportif (2-3 kalimat)",
    )
