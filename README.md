# MagadhAI-A-Multilingual-RAG-Powered-Meeting-Intelligence-Assistant

[

![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)

](https://gdcstg7kke3nm6m2xmfbv.streamlit.app)
![image alt](https://github.com/Srivastavarachit01/MagadhAI-A-Multilingual-RAG-Powered-Meeting-Intelligence-Assistant/blob/1f60788310f27d92e2933955656c1ab3e71a3177/andrea-de-santis-zwd435-ewb4-unsplash.jpg)
# 🎙️ MeetingMind — AI-Powered Meeting Transcription & Analysis

> Transcribe, summarise, and chat with your meetings — in English, Hindi, or Hinglish.

---

## What It Does

MeetingMind takes a YouTube URL or any local audio/video file and turns it into a fully structured meeting report — automatically. It handles transcription, summarisation, action item extraction, and even lets you ask questions about the meeting in natural language.

**Key capabilities:**

- Accepts YouTube URLs or local audio/video files as input
- Transcribes English meetings using OpenAI Whisper (runs locally, no API cost)
- Transcribes Hindi & Hinglish meetings using Sarvam AI
- Generates a concise bullet-point summary of the full meeting
- Extracts action items with assigned owners and deadlines
- Extracts key decisions made during the meeting
- Captures open questions and follow-up items
- Lets you **chat with your meeting** using RAG (Retrieval-Augmented Generation) powered by ChromaDB
- Exports the full report as a PDF or TXT file

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| English Transcription | OpenAI Whisper (local, free) |
| Hindi/Hinglish Transcription | Sarvam AI |
| LLM Pipeline | LangChain LCEL |
| Language Model | Mistral AI (free API tier) |
| Vector Database | ChromaDB |
| Embeddings | HuggingFace Sentence Transformers (local, free) |
| UI | Streamlit |

---

## Getting Started

### Prerequisites

- Python 3.9+
- FFmpeg (for audio extraction)
- A free [Mistral AI](https://mistral.ai) API key
- A [Sarvam AI](https://sarvam.ai) API key (for Hindi/Hinglish transcription)

### Installation

```bash
git clone https://github.com/your-username/meetingmind.git
cd meetingmind
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
MISTRAL_API_KEY=your_mistral_api_key
SARVAM_API_KEY=your_sarvam_api_key
```

### Run the App

```bash
streamlit run app.py
```

---

## Usage

1. Paste a YouTube URL or upload a local audio/video file
2. Select the meeting language (English / Hindi / Hinglish)
3. Click **Transcribe** and wait for processing
4. View the auto-generated summary, action items, decisions, and open questions
5. Use the **Chat** tab to ask questions about the meeting
6. Export the full report as PDF or TXT

---

## Project Structure

```
meetingmind/
├── app.py                  # Streamlit UI entry point
├── transcriber/
│   ├── whisper_engine.py   # English transcription via Whisper
│   └── sarvam_engine.py    # Hindi/Hinglish transcription via Sarvam AI
├── analyser/
│   ├── summariser.py       # Meeting summary generation
│   ├── action_items.py     # Action item extraction
│   └── decisions.py        # Decision and follow-up extraction
├── rag/
│   ├── embeddings.py       # HuggingFace embeddings
│   └── chat.py             # ChromaDB-backed RAG pipeline
├── exporter/
│   └── report.py           # PDF and TXT export
├── requirements.txt
└── .env.example
```

---

## Roadmap

- [ ] Speaker diarisation (who said what)
- [ ] Multi-language support beyond Hindi/English
- [ ] Google Meet / Zoom integration
- [ ] Slack/Notion export
- [ ] Scheduled meeting ingestion

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## License

[MIT](LICENSE)
