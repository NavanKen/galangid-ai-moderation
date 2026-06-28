from enum import StrEnum

class PromptIntro(StrEnum):
    MODERATION  = "Analisis campaign donasi berikut:"
    RECOMMENDATION = "Berikan saran perbaikan untuk campaign berikut:"
    FRAUD = "Analisis campaign berikut untuk mendeteksi potensi penipuan:"
    SUMMARY = "Buatkan ringkasan campaign berikut:"
    CATEGORIZATION = "Tentukan kategori campaign berikut:"
