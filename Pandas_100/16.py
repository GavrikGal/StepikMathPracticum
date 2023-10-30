import numpy as np
from data import df

new_index = "k"
new_data = [5.5, "dog", "Belka", "no", 2]
del_index = "f"

df = df.drop(del_index)
df = df.sort_index(axis=1)
df.loc[new_index] = new_data

print(df)