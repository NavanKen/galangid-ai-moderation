from pydantic import BaseModel, Field


class ScamDetectionRequest(BaseModel):
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


class ScamIndicator(BaseModel):
    type: str = Field(
        ...,
        description=(
            "Kode singkat pola mencurigakan, "
            "contoh: 'transfer_di_luar_platform', 'deskripsi_terlalu_singkat'"
        ),
    )
    description: str = Field(
        ...,
        description="Penjelasan mengapa pola ini dianggap mencurigakan",
    )
    severity: str = Field(
        ...,
        description="Tingkat keparahan: 'low', 'medium', atau 'high'",
    )


class ScamDetectionResponse(BaseModel):
    is_suspicious: bool = Field(
        ...,
        description="Apakah campaign terdeteksi mencurigakan",
    )
    confidence_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Seberapa yakin AI bahwa campaign mencurigakan (0=aman, 100=scam)",
    )
    risk_level: str = Field(
        ...,
        description="Level risiko: 'safe', 'low', 'medium', 'high', 'critical'",
    )
    indicators: list[ScamIndicator] = Field(
        default_factory=list,
        description="Daftar indikasi mencurigakan yang ditemukan (kosong jika aman)",
    )
    analysis: str = Field(
        ...,
        description="Penjelasan lengkap hasil analisis fraud",
    )
    recommendation: str = Field(
        ...,
        description="Rekomendasi aksi untuk admin",
    )
