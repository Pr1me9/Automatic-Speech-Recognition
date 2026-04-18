def normalize_numbers(text):
    num_map = {
        "एक": "1",
        "दो": "2",
        "तीन": "3",
        "चार": "4",
        "पांच": "5",
        "दस": "10",
        "सौ": "100",
        "हजार": "1000"
    }

    for k, v in num_map.items():
        text = text.replace(k, v)
    return text


def tag_english(text):
    english_words = ["टेंट", "कैम्प", "एरिया"]

    for word in english_words:
        text = text.replace(word, f"[EN]{word}[/EN]")

    return text


sample = "हम टेंट में रहे और दो दिन बाद लौटे"
print(normalize_numbers(sample))
print(tag_english(sample))