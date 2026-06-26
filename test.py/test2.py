import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.audio_processor import chunk_audio
from core.transcriber import transcribe_all

existing_file = "downloads/raamam.wav"  # Hindi/Telugu file

chunks = chunk_audio(existing_file)
transcript = transcribe_all(chunks, language="sa")  # "sa" for Sanskrit
print(transcript)