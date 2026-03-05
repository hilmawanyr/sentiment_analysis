from sklearn.feature_extraction.text import TfidfVectorizer

def build_vectorizer(
    max_features: int = 10000,
    ngram_range: tuple = (1, 2)
):
    return TfidfVectorizer(
        max_features=max_features,
        ngram_range=ngram_range,
        sublinear_tf=True
    )
