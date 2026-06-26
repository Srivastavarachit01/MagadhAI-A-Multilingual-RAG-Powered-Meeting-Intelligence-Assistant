import sys
import os
sys.path.insert(0, "/Users/srivrac10/Desktop/Video agent")

from utils.audio_processor import chunk_audio
from core.transcriber import transcribe_all

existing_file = "downloads/sooraj.wav"
chunks = chunk_audio(existing_file)
transcript = transcribe_all(chunks, language="hi")
print(transcript)