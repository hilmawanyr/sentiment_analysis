# %%
import pandas as pd
from src.util.split import stratified_split

# %%
df = pd.read_csv("../data/raw/tweet_pilpres_2019.csv")

# %%
df.head()

# %%
train_df, test_df = stratified_split(df, label_column="sentimen")

print("Train distribution")
print(train_df["sentimen"].value_counts(normalize=True))

print("Test distribution")
print(test_df["sentimen"].value_counts(normalize=True))
