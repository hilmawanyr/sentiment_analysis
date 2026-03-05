from sklearn.feature_extraction.text import TfidfVectorizer

def build_vectorizer(
    max_features: int = 10000,
    ngram_range: tuple = (1, 2),
    min_df: int = 2,
    max_df: float = 0.9
):
    return TfidfVectorizer(
        max_features=max_features,
        ngram_range=ngram_range,
        sublinear_tf=True,
        min_df=min_df,
        max_df=max_df
    )
