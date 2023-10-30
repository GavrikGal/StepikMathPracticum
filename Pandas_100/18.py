import numpy as np
from data import df

sort_by = ["age", "visits"]

df = df.sort_values(sort_by, ascending=[False, True])
print(df)