import pandas as pd
from sklearn.model_selection import train_test_split

def stratified_split(
    df: pd.DataFrame,
    label_column: str,
    test_size=0.15,
    val_size=0.15,
    random_state=42
):
    train_df, temp_df = train_test_split(
        df,
        test_size=test_size+val_size,
        stratify=df[label_column],
        random_state=random_state,
    )

    train_df = pd.DataFrame(train_df)
    temp_df = pd.DataFrame(temp_df)

    relative_val_size = val_size / (test_size + val_size)

    val_df, test_df = train_test_split(
        temp_df,
        test_size=1-relative_val_size,
        stratify=temp_df[label_column],
        random_state=random_state,
    )

    val_df = pd.DataFrame(val_df)
    test_df = pd.DataFrame(test_df)

    return train_df, val_df, test_df
