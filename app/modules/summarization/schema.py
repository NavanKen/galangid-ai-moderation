from pydantic import BaseModel, Field

class SummarizationRequest(BaseModel):
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


class SummarizationResponse(BaseModel):
    short_summary: str = Field(
        ...,
        description="Ringkasan 1 kalimat untuk preview/card (maks 50 kata)",
    )
    full_summary: str = Field(
        ...,
        description="Ringkasan lengkap 2-4 kalimat untuk admin (maks 100 kata)",
    )
    key_points: list[str] = Field(
        default_factory=list,
        description="3-5 poin penting yang diekstrak dari campaign",
    )
    beneficiary: str = Field(
        ...,
        description="Siapa penerima bantuan",
    )
    purpose: str = Field(
        ...,
        description="Tujuan penggunaan dana dalam 1 kalimat",
    )
    urgency_level: str = Field(
        ...,
        description="Tingkat urgensi: 'low', 'medium', 'high', 'critical'",
    )
