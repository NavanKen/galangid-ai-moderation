from pydantic import BaseModel, Field

class CategorizationRequest(BaseModel):
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
        description="Kategori yang dipilih pengguna (untuk validasi AI)",
    )


class AlternativeCategory(BaseModel):
    category: str = Field(
        ...,
        description="Nama kategori alternatif",
    )
    relevance: str = Field(
        ...,
        description="Penjelasan mengapa kategori ini juga relevan",
    )


class CategorizationResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="Kategori yang diprediksi AI",
    )
    confidence: int = Field(
        ...,
        ge=0,
        le=100,
        description="Tingkat keyakinan AI terhadap prediksi (0-100)",
    )
    reasoning: str = Field(
        ...,
        description="Alasan mengapa kategori ini dipilih",
    )
    alternative_categories: list[AlternativeCategory] = Field(
        default_factory=list,
        description="Kategori alternatif yang juga relevan",
    )
    matches_user_category: bool | None = Field(
        default=None,
        description="True jika prediksi AI sama dengan pilihan user, None jika user tidak memilih",
    )
