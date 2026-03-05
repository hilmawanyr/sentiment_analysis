import pandas as pd
from sklearn.model_selection import train_test_split

def stratified_split(
    df: pd.DataFrame,
    label_column: str,
    test_size=0.2,
    random_state=42
) -> tuple[pd.DataFrame, pd.DataFrame]:

    train_df, test_df = train_test_split(
        df,
        test_size=test_size,
        stratify=df[label_column],
        random_state=random_state,
    )

    train_df = pd.DataFrame(train_df)
    test_df = pd.DataFrame(test_df)

    return train_df, test_df
