import json

print("🚀 Training started...")

# load dataset
with open("clean_dataset.json", encoding="utf-8") as f:
    data = json.load(f)

print("✅ Dataset loaded")

print("📊 Dataset size:", len(data))

# simulate model loading
print("🤖 Loading Whisper model...")
print("✅ Model Loaded")

# simulate training
for i, d in enumerate(data):
    print(f"🔹 Training on sample {i+1}")

print("🎉 Training completed!")