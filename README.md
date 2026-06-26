# MagadhAI-A-Multilingual-RAG-Powered-Meeting-Intelligence-Assistant

[

![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)

](https://gdcstg7kke3nm6m2xmfbv.streamlit.app)
![image alt](https://github.com/Srivastavarachit01/MagadhAI-A-Multilingual-RAG-Powered-Meeting-Intelligence-Assistant/blob/1f60788310f27d92e2933955656c1ab3e71a3177/andrea-de-santis-zwd435-ewb4-unsplash.jpg)
<div align="center">

# 🪷 MagadhAI

### A Multilingual RAG-Powered Meeting Intelligence Assistant

*Turn every meeting — in English, Hindi, or Hinglish — into a searchable, summarised, and actionable record.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/Framework-LangChain%20LCEL-1C3C3C?style=flat-square)](https://www.langchain.com/)
[![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-4B8BBE?style=flat-square)](https://www.trychroma.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#-license)

[Overview](#-overview) • [Features](#-features) • [Tech Stack](#%EF%B8%8F-tech-stack) • [Architecture](#-architecture) • [Installation](#-installation) • [Usage](#-usage) • [Roadmap](#-roadmap) • [Contributing](#-contributing)

</div>

---

## 📖 Overview

**MagadhAI** is an end-to-end meeting intelligence assistant that converts raw conversations — from a YouTube link, a Zoom recording, or a local audio file — into structured, queryable knowledge.

Named after the ancient Indian empire renowned for its centres of learning, MagadhAI is built for a multilingual world. Most meeting-intelligence tools fall short the moment a conversation switches from English into Hindi or Hinglish. MagadhAI doesn't. It detects, transcribes, and understands meetings across languages, then lets you summarise, interrogate, and export them with the same ease.

Drop in a recording. Walk away with a summary, an action-item tracker, a decision log, and a chat interface that knows your meeting inside out.

---

## ✨ Features

| Capability | Description |
|---|---|
| 🎥 **Flexible Input** | Accepts any YouTube URL, or a local audio/video file, as the source recording |
| 🗣️ **English Transcription** | Transcribes English meetings locally using OpenAI's Whisper — no API costs, no data leaving your machine |
| 🇮🇳 **Hindi & Hinglish Transcription** | Routes Hindi and code-mixed Hinglish audio through Sarvam AI for accurate regional transcription |
| 📝 **Smart Summarisation** | Condenses the entire meeting into a clear, structured, bullet-point summary |
| ✅ **Action Item Extraction** | Identifies tasks discussed in the meeting, along with the responsible owner and deadline |
| 📌 **Decision Logging** | Pulls out every concrete decision made during the conversation |
| ❓ **Open Questions & Follow-ups** | Surfaces unresolved questions and items flagged for later discussion |
| 💬 **Chat With Your Meeting** | A Retrieval-Augmented Generation (RAG) interface, backed by ChromaDB, lets you ask follow-up questions about anything discussed |
| 📄 **Exportable Reports** | Generates a complete report of the meeting as a downloadable PDF or TXT file |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python |
| **English ASR** | OpenAI Whisper *(local, free)* |
| **Hindi/Hinglish ASR** | Sarvam AI |
| **Orchestration** | LangChain LCEL *(modern, composable pipelines)* |
| **LLM Inference** | Mistral AI *(free-tier API)* |
| **Vector Store** | ChromaDB |
| **Embeddings** | HuggingFace Embeddings *(local, free)* |
| **Interface** | Streamlit |

---

## 🏗️ Architecture

```
                       ┌─────────────────────┐
                       │   YouTube URL /      │
                       │   Audio/Video File   │
                       └──────────┬───────────┘
                                  │
                          Language Detected?
                                  │
                  ┌───────────────┴───────────────┐
                  │                               │
            English Audio                Hindi / Hinglish Audio
                  │                               │
        ┌─────────▼─────────┐         ┌───────────▼───────────┐
        │  Whisper (local)   │         │      Sarvam AI         │
        └─────────┬─────────┘         └───────────┬───────────┘
                  │                               │
                  └───────────────┬───────────────┘
                                  │
                          Full Transcript
                                  │
                    ┌─────────────▼─────────────┐
                    │     LangChain LCEL Chain   │
                    │   (Mistral AI as the LLM)  │
                    └─────────────┬─────────────┘
                                  │
        ┌────────────┬───────────┼───────────┬────────────┐
        │             │           │           │            │
   Summary      Action Items   Decisions   Open Q's   Embeddings
   (bullets)    (owner+due)     Log        & Follow-  → ChromaDB
                                            ups              │
                                                              │
                                                    ┌─────────▼─────────┐
                                                    │  RAG Chat Engine  │
                                                    │  (ask anything)   │
                                                    └─────────┬─────────┘
                                                              │
                                                    ┌─────────▼─────────┐
                                                    │  Streamlit UI +   │
                                                    │  PDF / TXT Export  │
                                                    └────────────────────┘
```

---

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- `ffmpeg` installed and available on your system `PATH` *(required by Whisper)*
- A [Sarvam AI](https://www.sarvam.ai/) API key *(for Hindi/Hinglish transcription)*
- A [Mistral AI](https://mistral.ai/) API key *(free tier available)*

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/MagadhAI-A-Multilingual-RAG-Powered-Meeting-Intelligence-Assistant.git
cd MagadhAI-A-Multilingual-RAG-Powered-Meeting-Intelligence-Assistant

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Open .env and add your SARVAM_API_KEY and MISTRAL_API_KEY

# 5. Launch the application
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🚀 Usage

1. **Provide your meeting** — paste a YouTube URL, or upload an audio/video file directly.
2. **Let MagadhAI listen** — the appropriate engine (Whisper or Sarvam AI) transcribes the recording based on the language detected.
3. **Review your intelligence report** — browse the auto-generated summary, action items, decisions, and open questions.
4. **Chat with your meeting** — ask natural-language questions like *"What did Priya commit to?"* or *"Were there any disagreements about the budget?"* and get answers grounded in the actual transcript.
5. **Export and share** — download the full report as a PDF or TXT file for your records or your team.

---

## 🗺️ Roadmap

- [ ] Speaker diarisation (who said what)
- [ ] Support for additional Indian languages (Tamil, Bengali, Marathi)
- [ ] Slack / Notion / Email integration for auto-sharing reports
- [ ] Multi-meeting search across a project's entire history
- [ ] Calendar integration for automated deadline tracking

---

## 🤝 Contributing

Contributions, issues, and feature requests are warmly welcomed.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please open an issue first to discuss any major changes you'd like to propose.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper) for robust, free, local speech recognition
- [Sarvam AI](https://www.sarvam.ai/) for pioneering Indian-language speech models
- [LangChain](https://www.langchain.com/) for making LLM pipelines composable
- [Mistral AI](https://mistral.ai/) for accessible, high-quality language models
- [ChromaDB](https://www.trychroma.com/) for a delightfully simple vector store
- [Streamlit](https://streamlit.io/) for turning Python scripts into real applications

---

<div align="center">

**Built with ❤️ for teams who meet in more than one language.**

If MagadhAI saved you time, consider giving the repository a ⭐

</div>
