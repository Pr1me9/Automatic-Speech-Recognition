import pandas as pd
import requests
import os
import json
from tqdm import tqdm

df = pd.read_csv("metadata.csv")

os.makedirs("data/audio", exist_ok=True)
os.makedirs("data/text", exist_ok=True)

def get_transcription_url(user_id, recording_id):
    return f"https://storage.googleapis.com/upload_goai/{user_id}/{recording_id}_transcription.json"

def get_audio_url(user_id, recording_id):
    return f"https://storage.googleapis.com/upload_goai/{user_id}/{recording_id}.wav"

def download(url, path):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            with open(path, "wb") as f:
                f.write(r.content)
    except:
        print("Error:", url)

dataset = []

for _, row in tqdm(df.iterrows(), total=len(df)):
    uid = row["user_id"]
    rid = row["recording_id"]

    audio_url = get_audio_url(uid, rid)
    text_url = get_transcription_url(uid, rid)

    audio_path = f"data/audio/{rid}.wav"
    text_path = f"data/text/{rid}.json"

    download(audio_url, audio_path)
    download(text_url, text_path)

    try:
        with open(text_path) as f:
            segments = json.load(f)

        full_text = " ".join([seg["text"] for seg in segments])

        dataset.append({
            "audio": audio_path,
            "text": full_text
        })
    except:
        continue

with open("dataset.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print("✅ Dataset created!")