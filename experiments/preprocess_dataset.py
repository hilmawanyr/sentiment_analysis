from src.preprocessing.preprocess_pipeline import preprocess_text

def preprocess_dataframe(df, text_column):
    df["clean_text"] = df[text_column].apply(preprocess_text)
    return df
