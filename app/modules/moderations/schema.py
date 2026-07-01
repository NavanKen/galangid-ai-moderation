from pydantic import BaseModel, Field

class CampaignModerationRequest(BaseModel):

    title: str = Field(
        ...,
        min_length=1,
        description="Judul campaign",
        examples=["Bantu Operasi Jantung Ayah Saya"],
    )
    description: str = Field(
        ...,
        min_length=1,
        description="Deskripsi lengkap campaign",
        examples=[
            "Ayah saya didiagnosis membutuhkan operasi bypass jantung. "
            "Biaya operasi mencapai Rp 150 juta. Kami sudah mengumpulkan "
            "sebagian dari tabungan keluarga, namun masih kurang Rp 80 juta."
        ],
    )
    goal_amount: int | None = Field(
        default=None,
        gt=0,
        description="Target donasi dalam Rupiah",
        examples=[80000000],
    )
    category: str | None = Field(
        default=None,
        description="Kategori yang dipilih pengguna (opsional, akan divalidasi AI)",
        examples=["Kesehatan"],
    )

class CampaignModerationResponse(BaseModel):
    """Response terstruktur yang dikembalikan ke NestJS."""

    approved: bool = Field(
        ...,
        description="Apakah campaign layak dipublikasikan",
    )
    risk_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Skor risiko campaign (0=sangat aman, 100=risiko tinggi)",
    )
    category: str = Field(
        ...,
        description="Kategori campaign hasil analisis AI",
    )
    summary: str = Field(
        ...,
        description="Ringkasan campaign dalam 1-3 kalimat",
    )
    reason: str = Field(
        ...,
        description="Alasan utama penilaian AI",
    )
    scam_indicators: list[str] = Field(
        default_factory=list,
        description="Daftar indikasi mencurigakan (kosong jika tidak ada)",
    )
    suggestions: list[str] = Field(
        default_factory=list,
        description="Saran perbaikan untuk campaign (maks 5)",
    )