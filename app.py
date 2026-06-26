"""
Video Agent — Premium Streamlit UI
Drop this file at the root of your project (same level as core/ and utils/).
Run: streamlit run app.py
"""

import streamlit as st
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


# ─────────────────────────────────────────────────────────────────────────────
# Page config — must be first Streamlit call
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Video Agent",
    page_icon="🎙",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700&family=Inter:wght@300;400;500;600&family=Fira+Code:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"], .stApp {
    background: #08090D !important;
    font-family: 'Inter', sans-serif;
    color: #FAFAFA;
}

#MainMenu, header, footer, [data-testid="stToolbar"] { visibility: hidden !important; }

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Topbar ── */
.va-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 18px 48px 18px 40px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    background: #08090D;
    position: sticky;
    top: 0;
    z-index: 100;
}
.va-logo {
    display: flex;
    align-items: center;
    gap: 10px;
}
.va-logo-mark {
    width: 34px; height: 34px;
    background: linear-gradient(135deg, #7C3AED, #C026D3);
    border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px;
    box-shadow: 0 0 20px rgba(124,58,237,0.4);
}
.va-logo-name {
    font-family: 'Sora', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #FAFAFA;
    letter-spacing: -0.3px;
}
.va-logo-tag {
    font-size: 0.7rem;
    color: #6B7280;
}
.va-topbar-right {
    font-size: 0.72rem;
    color: #374151;
    font-family: 'Fira Code', monospace;
}

/* ── Page wrapper ── */
.va-page {
    max-width: 1120px;
    margin: 0 auto;
    padding: 48px 40px 120px 40px;
}

/* ── Hero ── */
.va-hero { margin-bottom: 44px; }
.va-hero-eyebrow {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #7C3AED;
    margin-bottom: 10px;
}
.va-hero-title {
    font-family: 'Sora', sans-serif;
    font-size: 2.4rem;
    font-weight: 700;
    letter-spacing: -0.8px;
    line-height: 1.15;
    color: #FAFAFA;
    margin-bottom: 10px;
}
.va-hero-title span {
    background: linear-gradient(90deg, #7C3AED, #C026D3);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.va-hero-sub {
    font-size: 0.88rem;
    color: #6B7280;
    line-height: 1.6;
    max-width: 520px;
}

/* ── Input card ── */
.va-input-card {
    background: #0F1117;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 32px;
    box-shadow: 0 4px 40px rgba(0,0,0,0.5);
}

.stTextInput > div > div > input {
    background: #161B27 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
    color: #FAFAFA !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.9rem !important;
    padding: 12px 16px !important;
    height: auto !important;
}
.stTextInput > div > div > input:focus {
    border-color: #7C3AED !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.18) !important;
}
.stTextInput > div > div > input::placeholder { color: #374151 !important; }

.stSelectbox > div > div {
    background: #161B27 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
    color: #FAFAFA !important;
}

div[data-testid="stWidgetLabel"] > label {
    color: #6B7280 !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
}

/* ── Buttons ── */
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #7C3AED, #C026D3) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Sora', sans-serif !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    padding: 13px 28px !important;
    width: 100% !important;
    box-shadow: 0 4px 24px rgba(124,58,237,0.35) !important;
    transition: all 0.25s ease !important;
}
div[data-testid="stButton"] > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(124,58,237,0.5) !important;
}

.btn-secondary div[data-testid="stButton"] > button {
    background: #161B27 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    box-shadow: none !important;
    color: #9CA3AF !important;
    font-size: 0.78rem !important;
    padding: 9px 16px !important;
}
.btn-secondary div[data-testid="stButton"] > button:hover {
    background: #1F2937 !important;
    color: #FAFAFA !important;
    transform: none !important;
    box-shadow: none !important;
}

/* ── Pipeline ── */
.va-pipeline { margin: 0 0 44px 0; }
.va-pipeline-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #374151;
    margin-bottom: 16px;
}
.va-wave-track {
    display: flex;
    align-items: center;
    background: #0F1117;
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 14px;
    padding: 20px 28px;
}
.va-node-group {
    display: flex;
    align-items: center;
    flex: 1;
}
.va-node-group:last-child { flex: 0; }
.va-node {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
}
.va-node-dot {
    width: 42px; height: 42px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 17px;
    transition: all 0.4s ease;
}
.va-node-dot.pending {
    background: #161B27;
    border: 1.5px solid #1F2937;
    color: #374151;
}
.va-node-dot.active {
    background: linear-gradient(135deg, rgba(124,58,237,0.25), rgba(192,38,211,0.25));
    border: 1.5px solid #7C3AED;
    color: #A78BFA;
    box-shadow: 0 0 0 8px rgba(124,58,237,0.08), 0 0 24px rgba(124,58,237,0.35);
    animation: nodebeat 1.8s ease-in-out infinite;
}
.va-node-dot.done {
    background: linear-gradient(135deg, #064E3B, #065F46);
    border: 1.5px solid #10B981;
    color: #34D399;
    box-shadow: 0 0 14px rgba(16,185,129,0.25);
}
.va-node-dot.error {
    background: rgba(127,29,29,0.4);
    border: 1.5px solid #DC2626;
    color: #F87171;
}
@keyframes nodebeat {
    0%,100% { box-shadow: 0 0 0 0 rgba(124,58,237,0.5), 0 0 20px rgba(124,58,237,0.2); }
    50%      { box-shadow: 0 0 0 12px rgba(124,58,237,0.0), 0 0 32px rgba(124,58,237,0.45); }
}
.va-node-name {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-align: center;
    white-space: nowrap;
}
.va-node-name.pending { color: #374151; }
.va-node-name.active  { color: #A78BFA; }
.va-node-name.done    { color: #34D399; }
.va-node-name.error   { color: #F87171; }

.va-dash {
    flex: 1;
    height: 2px;
    margin: 0 10px;
    margin-bottom: 22px;
    background: #1F2937;
    border-radius: 2px;
    position: relative;
    overflow: hidden;
}
.va-dash::after {
    content: '';
    position: absolute;
    top: 0; left: 0; height: 100%; width: 0%;
    background: linear-gradient(90deg, #7C3AED, #C026D3);
    border-radius: 2px;
    transition: width 0.6s ease;
}
.va-dash.done::after { width: 100%; }
.va-dash.active::after {
    animation: dashmarch 1.2s ease-in-out infinite alternate;
}
@keyframes dashmarch {
    from { width: 25%; opacity: 0.6; }
    to   { width: 75%; opacity: 1.0; }
}

/* ── Results ── */
.va-results-header {
    display: flex;
    align-items: baseline;
    gap: 14px;
    margin-bottom: 6px;
}
.va-results-title {
    font-family: 'Sora', sans-serif;
    font-size: 1.55rem;
    font-weight: 700;
    letter-spacing: -0.4px;
    color: #FAFAFA;
}
.va-results-sub { font-size: 0.78rem; color: #6B7280; }
.va-divider {
    height: 1px;
    background: rgba(255,255,255,0.06);
    margin: 16px 0 28px 0;
}

.va-stat-strip {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 28px;
}
.va-stat {
    background: #0F1117;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 8px;
    padding: 8px 14px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.va-stat-num {
    font-family: 'Sora', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #A78BFA;
}
.va-stat-label { font-size: 0.72rem; color: #6B7280; font-weight: 500; }

/* ── Cards ── */
.va-card {
    background: #0F1117;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    padding: 24px 26px;
    height: 100%;
    transition: border-color 0.25s;
}
.va-card:hover { border-color: rgba(255,255,255,0.12); }
.va-card-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 16px;
    padding-bottom: 14px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.va-card-icon {
    width: 32px; height: 32px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px;
    flex-shrink: 0;
}
.va-card-title {
    font-family: 'Sora', sans-serif;
    font-size: 0.82rem;
    font-weight: 700;
    color: #E5E7EB;
}
.va-card-subtitle { font-size: 0.68rem; color: #4B5563; margin-top: 1px; }
.va-card-body {
    font-size: 0.84rem;
    color: #9CA3AF;
    line-height: 1.85;
    white-space: pre-wrap;
}
.icon-purple { background: rgba(124,58,237,0.15); }
.icon-indigo { background: rgba(99,102,241,0.12); }
.icon-green  { background: rgba(16,185,129,0.12); }
.icon-amber  { background: rgba(245,158,11,0.12); }
.icon-rose   { background: rgba(244,63,94,0.12); }

/* ── Transcript mono ── */
.va-transcript {
    font-family: 'Fira Code', monospace;
    font-size: 0.78rem;
    line-height: 1.85;
    color: #6B7280;
    max-height: 270px;
    overflow-y: auto;
    padding-right: 8px;
}
.va-transcript::-webkit-scrollbar { width: 4px; }
.va-transcript::-webkit-scrollbar-thumb { background: #1F2937; border-radius: 4px; }

/* ── Chat panel ── */
.va-chat-wrapper {
    background: #0F1117;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 26px 28px 20px 28px;
    margin-top: 28px;
    position: relative;
    box-shadow: 0 -4px 40px rgba(0,0,0,0.35);
}
.va-chat-glow {
    position: absolute;
    top: -1px; left: 50%;
    transform: translateX(-50%);
    width: 200px; height: 2px;
    background: linear-gradient(90deg, transparent, #7C3AED, #C026D3, transparent);
}
.va-chat-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.va-chat-orb {
    width: 30px; height: 30px;
    background: linear-gradient(135deg, #7C3AED, #C026D3);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px;
    box-shadow: 0 0 16px rgba(124,58,237,0.45);
}
.va-chat-title {
    font-family: 'Sora', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    color: #E5E7EB;
}
.va-chat-sub { font-size: 0.7rem; color: #4B5563; }

.va-messages {
    display: flex;
    flex-direction: column;
    gap: 12px;
    max-height: 400px;
    overflow-y: auto;
    padding-right: 6px;
    margin-bottom: 4px;
}
.va-messages::-webkit-scrollbar { width: 4px; }
.va-messages::-webkit-scrollbar-thumb { background: #1F2937; border-radius: 4px; }

.va-msg-row-user { display: flex; justify-content: flex-end; }
.va-msg-row-bot  { display: flex; justify-content: flex-start; }

.va-bubble-user {
    background: linear-gradient(135deg, #4C1D95, #6D28D9);
    color: #EDE9FE;
    padding: 11px 16px;
    border-radius: 14px 14px 3px 14px;
    font-size: 0.83rem;
    line-height: 1.65;
    max-width: 72%;
    border: 1px solid rgba(167,139,250,0.2);
}
.va-bubble-bot {
    background: #161B27;
    color: #D1D5DB;
    padding: 12px 16px;
    border-radius: 3px 14px 14px 14px;
    font-size: 0.83rem;
    line-height: 1.75;
    max-width: 82%;
    border: 1px solid rgba(255,255,255,0.07);
}

/* ── Download btn ── */
div[data-testid="stDownloadButton"] > button {
    background: #161B27 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    color: #9CA3AF !important;
    font-size: 0.78rem !important;
    font-family: 'Inter', sans-serif !important;
    border-radius: 8px !important;
    padding: 8px 16px !important;
    box-shadow: none !important;
    width: auto !important;
}
div[data-testid="stDownloadButton"] > button:hover {
    background: #1F2937 !important;
    color: #FAFAFA !important;
    transform: none !important;
    box-shadow: none !important;
}

div[data-testid="stAlert"] {
    background: rgba(127,29,29,0.25) !important;
    border: 1px solid rgba(220,38,38,0.4) !important;
    border-radius: 10px !important;
    color: #FCA5A5 !important;
    font-size: 0.83rem !important;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Session state
# ─────────────────────────────────────────────────────────────────────────────
for key, val in {
    "result": None,
    "chat_history": [],
    "pipeline_stage": "idle",
    "stage_statuses": {
        "audio": "pending", "transcribe": "pending",
        "analyze": "pending", "rag": "pending",
    },
    "error_msg": None,
    "source_cache": "",
    "lang_cache": "english",
}.items():
    if key not in st.session_state:
        st.session_state[key] = val


# ─────────────────────────────────────────────────────────────────────────────
# Top bar
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="va-topbar">
  <div class="va-logo">
    <div class="va-logo-mark">🎙</div>
    <div>
      <div class="va-logo-name">Video Agent</div>
      <div class="va-logo-tag">AI meeting intelligence</div>
    </div>
  </div>
  <div class="va-topbar-right">faster-whisper · mistral · chromadb</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="va-page">', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# Hero
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="va-hero">
  <div class="va-hero-eyebrow">AI Meeting Intelligence</div>
  <div class="va-hero-title">
    Turn any video into<br><span>structured insight.</span>
  </div>
  <div class="va-hero-sub">
    Paste a YouTube link or a local file path. Video Agent transcribes,
    summarises, and lets you chat with the content — in English or Hinglish.
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# Input card
# ─────────────────────────────────────────────────────────────────────────────
st.markdown('<div class="va-input-card">', unsafe_allow_html=True)
col_src, col_lang, col_btn = st.columns([3.5, 1.2, 1.1], gap="medium")
with col_src:
    source_input = st.text_input(
        "Source",
        placeholder="https://youtube.com/watch?v=...  or  /path/to/audio.mp3",
        key="source_field",
    )
with col_lang:
    language = st.selectbox("Language", ["english", "hinglish"], key="lang_field")
with col_btn:
    st.markdown("<div style='padding-top:24px;'>", unsafe_allow_html=True)
    run_clicked = st.button("▶  Analyse", key="run_btn")
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Pipeline waveform renderer
# ─────────────────────────────────────────────────────────────────────────────
STEPS = [
    ("audio",      "🔊", "Audio"),
    ("transcribe", "📝", "Transcribe"),
    ("analyze",    "🧠", "Analyse"),
    ("rag",        "💬", "RAG Index"),
]

def render_pipeline():
    ss = st.session_state.stage_statuses
    nodes_html = ""
    for i, (key, icon, name) in enumerate(STEPS):
        status = ss[key]
        dot_icon = {"done": "✓", "error": "✕"}.get(status, icon)
        nodes_html += f"""
        <div class="va-node-group">
          <div class="va-node">
            <div class="va-node-dot {status}">{dot_icon}</div>
            <div class="va-node-name {status}">{name}</div>
          </div>
        """
        if i < len(STEPS) - 1:
            dash_extra = "done" if status == "done" else ("active" if status == "active" else "")
            nodes_html += f'<div class="va-dash {dash_extra}"></div>'
        nodes_html += "</div>"

    return f"""
    <div class="va-pipeline">
      <div class="va-pipeline-label">Pipeline status</div>
      <div class="va-wave-track">{nodes_html}</div>
    </div>"""

pipeline_ph = st.empty()
pipeline_ph.markdown(render_pipeline(), unsafe_allow_html=True)

if st.session_state.error_msg:
    st.error(f"Pipeline error — {st.session_state.error_msg}")

# ─────────────────────────────────────────────────────────────────────────────
# Trigger
# ─────────────────────────────────────────────────────────────────────────────
if run_clicked and source_input.strip():
    st.session_state.error_msg = None
    st.session_state.result = None
    st.session_state.chat_history = []
    st.session_state.pipeline_stage = "running"
    st.session_state.source_cache = source_input.strip()
    st.session_state.lang_cache = language
    for k in st.session_state.stage_statuses:
        st.session_state.stage_statuses[k] = "pending"
    st.rerun()
elif run_clicked:
    st.warning("Enter a YouTube URL or file path first.")

# ─────────────────────────────────────────────────────────────────────────────
# Pipeline execution
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.pipeline_stage == "running":
    source = st.session_state.source_cache
    lang   = st.session_state.lang_cache
    try:
        from utils.audio_processor import process_input
        from core.transcriber     import transcribe_all
        from core.summarizer      import summarize, generate_title
        from core.extractor       import (extract_action_items,
                                          extract_key_decisions, extract_questions)
        from core.rag_engine      import build_rag_chain

        spin = st.empty()

        def step(key, label, fn, *args):
            st.session_state.stage_statuses[key] = "active"
            pipeline_ph.markdown(render_pipeline(), unsafe_allow_html=True)
            with spin:
                with st.spinner(label):
                    result = fn(*args)
            st.session_state.stage_statuses[key] = "done"
            return result

        chunks     = step("audio",      "Processing audio…",             process_input, source)
        transcript = step("transcribe", "Transcribing with Whisper…",    transcribe_all, chunks, lang)

        st.session_state.stage_statuses["analyze"] = "active"
        pipeline_ph.markdown(render_pipeline(), unsafe_allow_html=True)
        with spin:
            with st.spinner("Analysing with Mistral…"):
                title       = generate_title(transcript)
                summary     = summarize(transcript)
                action_item = extract_action_items(transcript)
                decisions   = extract_key_decisions(transcript)
                questions   = extract_questions(transcript)
        st.session_state.stage_statuses["analyze"] = "done"

        rag_chain  = step("rag",        "Building RAG index…",           build_rag_chain, transcript)
        spin.empty()

        pipeline_ph.markdown(render_pipeline(), unsafe_allow_html=True)
        st.session_state.result = dict(
            title=title, transcript=transcript, summary=summary,
            action_items=action_item, key_decisions=decisions,
            open_questions=questions, rag_chain=rag_chain,
        )
        st.session_state.pipeline_stage = "done"
        st.rerun()

    except Exception as exc:
        for k, v in st.session_state.stage_statuses.items():
            if v == "active":
                st.session_state.stage_statuses[k] = "error"
        st.session_state.error_msg = str(exc)
        st.session_state.pipeline_stage = "error"
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# Results
# ─────────────────────────────────────────────────────────────────────────────
result = st.session_state.result

if result:
    transcript = result["transcript"]
    word_count = len(transcript.split())
    sent_count = transcript.count(".") + transcript.count("।")

    st.markdown(f"""
    <div class="va-results-header">
      <div class="va-results-title">{result['title']}</div>
      <div class="va-results-sub">Analysis complete</div>
    </div>
    <div class="va-divider"></div>
    <div class="va-stat-strip">
      <div class="va-stat"><div class="va-stat-num">{word_count:,}</div><div class="va-stat-label">words</div></div>
      <div class="va-stat"><div class="va-stat-num">{sent_count}</div><div class="va-stat-label">sentences</div></div>
      <div class="va-stat"><div class="va-stat-num">{st.session_state.lang_cache.capitalize()}</div><div class="va-stat-label">language</div></div>
      <div class="va-stat"><div class="va-stat-num" style="color:#34D399;">✓</div><div class="va-stat-label">RAG ready</div></div>
    </div>
    """, unsafe_allow_html=True)

    # Row 1 — Summary + Transcript
    c1, c2 = st.columns([1.3, 1], gap="medium")
    with c1:
        st.markdown(f"""
        <div class="va-card">
          <div class="va-card-header">
            <div class="va-card-icon icon-purple">📋</div>
            <div><div class="va-card-title">Summary</div>
            <div class="va-card-subtitle">AI-generated overview</div></div>
          </div>
          <div class="va-card-body">{result['summary']}</div>
        </div>""", unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="va-card">
          <div class="va-card-header">
            <div class="va-card-icon icon-indigo">📄</div>
            <div><div class="va-card-title">Transcript</div>
            <div class="va-card-subtitle">Whisper large-v3 · raw output</div></div>
          </div>
          <div class="va-transcript">{transcript}</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("<div style='margin-top:8px;'>", unsafe_allow_html=True)
        st.download_button("⬇ Download transcript", data=transcript,
                           file_name="transcript.txt", mime="text/plain", key="dl_btn")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)

    # Row 2 — Actions · Decisions · Questions
    c3, c4, c5 = st.columns(3, gap="medium")
    with c3:
        st.markdown(f"""
        <div class="va-card">
          <div class="va-card-header">
            <div class="va-card-icon icon-green">✅</div>
            <div><div class="va-card-title">Action Items</div>
            <div class="va-card-subtitle">Things to follow up on</div></div>
          </div>
          <div class="va-card-body">{result['action_items']}</div>
        </div>""", unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="va-card">
          <div class="va-card-header">
            <div class="va-card-icon icon-amber">🔑</div>
            <div><div class="va-card-title">Key Decisions</div>
            <div class="va-card-subtitle">What was agreed</div></div>
          </div>
          <div class="va-card-body">{result['key_decisions']}</div>
        </div>""", unsafe_allow_html=True)

    with c5:
        st.markdown(f"""
        <div class="va-card">
          <div class="va-card-header">
            <div class="va-card-icon icon-rose">❓</div>
            <div><div class="va-card-title">Open Questions</div>
            <div class="va-card-subtitle">Still unresolved</div></div>
          </div>
          <div class="va-card-body">{result['open_questions']}</div>
        </div>""", unsafe_allow_html=True)

    # Chat panel
    from core.rag_engine import ask_question

    st.markdown("""
    <div class="va-chat-wrapper">
      <div class="va-chat-glow"></div>
      <div class="va-chat-header">
        <div class="va-chat-orb">✦</div>
        <div>
          <div class="va-chat-title">Ask the meeting</div>
          <div class="va-chat-sub">ChromaDB + Mistral RAG · English &amp; Hinglish</div>
        </div>
      </div>""", unsafe_allow_html=True)

    if st.session_state.chat_history:
        msgs_html = '<div class="va-messages">'
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                msgs_html += f'<div class="va-msg-row-user"><div class="va-bubble-user">{msg["content"]}</div></div>'
            else:
                msgs_html += f'<div class="va-msg-row-bot"><div class="va-bubble-bot">{msg["content"]}</div></div>'
        msgs_html += "</div>"
        st.markdown(msgs_html, unsafe_allow_html=True)
    else:
        st.markdown("""<div style="color:#374151;font-size:0.8rem;padding:4px 0 18px 0;font-style:italic;">
          No messages yet — ask anything about the meeting above.
        </div>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    chat_col, send_col, clear_col = st.columns([5.5, 0.9, 0.9], gap="small")
    with chat_col:
        user_q = st.text_input("Ask", placeholder="What were the main takeaways?  /  किस बात पर सबसे ज़्यादा बात हुई?",
                               key="chat_input", label_visibility="collapsed")
    with send_col:
        send = st.button("Send →", key="send_btn")
    with clear_col:
        st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
        clear = st.button("Clear", key="clear_btn")
        st.markdown("</div>", unsafe_allow_html=True)

    if send and user_q.strip():
        q = user_q.strip()
        st.session_state.chat_history.append({"role": "user", "content": q})
        with st.spinner(""):
            try:
                answer = ask_question(result["rag_chain"], q)
            except Exception as e:
                answer = f"Error: {e}"
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        st.rerun()

    if clear and st.session_state.chat_history:
        st.session_state.chat_history = []
        st.rerun()

else:
    if st.session_state.pipeline_stage == "idle":
        st.markdown("""
        <div style="text-align:center; padding:72px 0; color:#374151;">
          <div style="font-size:3rem; margin-bottom:16px; opacity:0.4;">🎙</div>
          <div style="font-family:'Sora',sans-serif; font-size:1rem; font-weight:600;
                      color:#4B5563; margin-bottom:8px;">No analysis yet</div>
          <div style="font-size:0.82rem; line-height:1.7; max-width:360px; margin:0 auto;">
            Enter a YouTube URL or a local audio file path above,
            then click <strong style="color:#A78BFA;">Analyse</strong>.
          </div>
        </div>""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
