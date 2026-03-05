from preprocessing.cleaner import clean_text
from preprocessing.stopwords import remove_stopwords
from preprocessing.stemmer import stem_text

def preprocess_text(text: str) -> str:
    text = clean_text(text)
    text = remove_stopwords(text)
    text = stem_text(text)
    return text
