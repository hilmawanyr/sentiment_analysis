from src.vectorization.tfidf_vectorizer import build_vectorizer

def vectorize_data(X_train, X_val, X_test):
    vectorizer = build_vectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_val_vec = vectorizer.transform(X_val)
    X_test_vec = vectorizer.transform(X_test)
    return X_train_vec, X_val_vec, X_test_vec, vectorizer
