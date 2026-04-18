import json
from collections import Counter

with open("clean_dataset.json", encoding="utf-8") as f:
    dataset = json.load(f)

words = []

for d in dataset:
    words.extend(d["text"].split())

counter = Counter(words)

def classify(word):
    if counter[word] > 5:
        return "correct", "high"
    else:
        return "incorrect", "low"

for w in list(counter.keys())[:20]:
    print(w, classify(w))