# 🤖 GalangID AI Moderation Service

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-green?style=for-the-badge&logo=fastapi)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge&logo=google)
![Pydantic](https://img.shields.io/badge/Pydantic-2.13-red?style=for-the-badge&logo=pydantic)
![License](https://img.shields.io/badge/License-MIT-black?style=for-the-badge)

**AI Moderation Service** untuk platform crowdfunding **GalangID**.

Service ini dirancang sebagai microservice AI independen yang menganalisis campaign donasi sebelum dipublikasikan. Menggunakan **Google Gemini** sebagai AI engine, service ini memberikan hasil moderasi berupa risk assessment, ringkasan campaign, prediksi kategori, deteksi indikasi penipuan, dan saran perbaikan.

---

## ✨ Features

- 🔍 **AI-Powered Campaign Moderation** — analisis campaign secara otomatis menggunakan Gemini AI
- 📊 **Risk Score Analysis** — skor risiko 0-100 untuk setiap campaign
- 📝 **Campaign Summary** — ringkasan otomatis isi campaign
- 💡 **AI-Generated Suggestions** — saran perbaikan agar campaign lebih kredibel
- 🏷️ **Category Prediction** — prediksi kategori campaign berdasarkan konten
- 🚨 **Scam Indicators Detection** — deteksi pola-pola mencurigakan
- 🧩 **Modular Architecture** — setiap fitur AI dipisah menjadi modul independen
- 💉 **Dependency Injection** — menggunakan FastAPI `Depends()` untuk DI

---

## 🛠 Tech Stack

| Technology | Deskripsi |
|---|---|
| **FastAPI** | Web framework untuk REST API |
| **Python 3.13** | Runtime |
| **Pydantic v2** | Data validation & serialization |
| **Google Gemini API** | AI engine untuk analisis |
| **Uvicorn** | ASGI server |

---

## 📂 Project Structure

```
galangid-ai-moderation/
│
├── app/
│   ├── config/
│   │   ├── ai/
│   │   │   ├── prompt_builder.py    # Builder untuk user prompt
│   │   │   └── prompt_intro.py      # Template intro prompt per modul
│   │   ├── config.py                # Settings (env variables)
│   │   ├── exceptions.py            # Custom exceptions
│   │   └── gemini.py                # Gemini client instance
│   │
│   ├── modules/
│   │   ├── base_service.py          # Base AI service (shared Gemini call)
│   │   ├── moderations/             # ✅ Campaign moderation module
│   │   │   ├── dependencies.py
│   │   │   ├── prompt.py            # System prompt untuk moderasi
│   │   │   ├── router.py            # POST /moderations/analyze
│   │   │   ├── schema.py            # Request & Response schema
│   │   │   └── service.py           # Business logic
│   │   ├── categorization/          # 🚧 Auto categorization
│   │   ├── recommendation/          # 🚧 Campaign recommendation
│   │   ├── scam_detection/          # 🚧 Advanced scam detection
│   │   └── summarization/           # 🚧 Campaign summarization
│   │
│   ├── app.py                       # FastAPI app factory
│   ├── main.py                      # Entry point
│   └── routers.py                   # Router registration
│
├── .env                             # Environment variables
├── requirements.txt                 # Python dependencies
├── pyproject.toml                   # Project metadata
└── vercel.json                      # Vercel deployment config
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- Google Gemini API Key

### Clone Repository

```bash
git clone https://github.com/username/galangid-ai-moderation.git
cd galangid-ai-moderation
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Buat file `.env` di root project:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

### Run Development Server

```bash
uvicorn app.main:app --reload
```

Server akan berjalan di `http://localhost:8000`.

### Swagger UI (API Docs)

```
http://localhost:8000/docs
```

---

## 📡 API Endpoints

### `POST /moderations/analyze`

Analisis campaign menggunakan AI.

**Request Body:**

```json
{
  "title": "Bantu Operasi Jantung Ayah Saya",
  "description": "Ayah saya didiagnosis membutuhkan operasi bypass jantung...",
  "goal_amount": 80000000,
  "category": "Kesehatan"
}
```

**Response:**

```json
{
  "approved": false,
  "risk_score": 65,
  "category": "Kesehatan",
  "summary": "Campaign ini bertujuan menggalang dana sebesar Rp 80 juta...",
  "reason": "Campaign memiliki tujuan yang jelas namun informasi sangat minim...",
  "scam_indicators": [
    "Deskripsi terlalu singkat...",
    "Klaim belum didukung bukti..."
  ],
  "suggestions": [
    "Sertakan surat diagnosis medis resmi...",
    "Lampirkan rincian estimasi biaya..."
  ]
}
```

---

## 📌 Current Modules

| Modul | Status | Deskripsi |
|---|---|---|
| **Moderation** | ✅ Selesai | Analisis & moderasi campaign |
| **Categorization** | 🚧 In Progress | Prediksi kategori otomatis |
| **Recommendation** | 🚧 In Progress | Rekomendasi campaign serupa |
| **Scam Detection** | 🚧 In Progress | Deteksi penipuan lanjutan |
| **Summarization** | 🚧 In Progress | Ringkasan campaign otomatis |

---

## 🏗 Architecture

```
Frontend (Next.js)
        │
        ▼
Backend (NestJS)
        │
        ▼
AI Moderation Service (FastAPI)  ◄── Service ini
        │
        ▼
Google Gemini API
```

FastAPI service dirancang sebagai **microservice AI independen** yang berkomunikasi dengan backend NestJS melalui REST API. Service ini:

- ❌ Tidak mengetahui siapa user/campaigner
- ❌ Tidak mengakses database GalangID
- ❌ Tidak memvalidasi JWT
- ✅ Hanya menerima data campaign untuk dianalisis
- ✅ Mengembalikan hasil analisis dalam format JSON terstruktur

---

## 📍 Roadmap

- [x] FastAPI setup & project structure
- [x] Modular architecture
- [x] Dependency Injection pattern
- [x] Gemini AI integration
- [x] Campaign moderation module
- [x] NestJS backend integration
- [ ] Recommendation module
- [ ] Advanced scam detection
- [ ] Auto categorization
- [ ] Campaign summarization
- [ ] OCR verification untuk bukti pendukung
- [ ] Rate limiting & caching

---

## 📄 License

This project is part of the **GalangID** ecosystem and is intended for educational purposes and portfolio development.
