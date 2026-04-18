print("🔥 FILE STARTED")
import json
import re

print("🚀 Script started")

with open("dataset.json", encoding="utf-8") as f:
    dataset = json.load(f)

print("✅ Dataset loaded:", len(dataset))

def clean_text(text):
    text = re.sub(r"(.)\1+", r"\1", text)
    text = re.sub(r"[^\u0900-\u097F\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

for d in dataset:
    d["text"] = clean_text(d["text"])

print("✅ Cleaning done")

with open("clean_dataset.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print("✅ File saved as clean_dataset.json")