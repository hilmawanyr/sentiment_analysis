import re

def clean_text(text: str) -> str:
    text = text.lower()

    # remove URL
    text = re.sub(r"http\S+|www\S+", "", text)

    # remove mention
    text = re.sub(r"@\w+", "", text)

    # remove hashtag symbol
    text = re.sub(r"#", "", text)

    # remove number
    text = re.sub(r"\d+", "", text)

    # remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text
