import sys, os
sys.path.insert(0, "/Users/srivrac10/Desktop/Video agent")

from dotenv import load_dotenv
load_dotenv("/Users/srivrac10/Desktop/Video agent/.env")

from utils.audio_processor import process_input
from core.transcriber import transcribe_all

load_dotenv()

source = "https://youtu.be/vFP1mgZ_LEY?si=oWiJbC0_sqi4oC7P"
language = "hinglish"  # change to "hinglish" to test Sarvam

chunks = process_input(source)
transcript = transcribe_all(chunks, language=language)

print("\n=== TRANSCRIPT ===\n")
print(transcript)