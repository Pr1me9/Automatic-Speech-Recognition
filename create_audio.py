import wave
import os

# ensure folder exists
os.makedirs("data/audio", exist_ok=True)

output_path = "data/audio/825780.wav"

# create dummy audio (1 second silence)
with wave.open(output_path, "w") as f:
    f.setnchannels(1)      # mono
    f.setsampwidth(2)      # 16-bit
    f.setframerate(16000) # 16kHz
    f.writeframes(b'\x00\x00' * 16000)

print("✅ Dummy audio created at:", output_path)