import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.audio_processor import convert_to_wav, chunk_audio
from core.transcriber import transcribe_all

# Already downloaded file use karo
existing_file = "downloads/The 7 Skills You Need to Build AI Agents.wav"

chunks = chunk_audio(existing_file)
transcript = transcribe_all(chunks)
print(transcript)