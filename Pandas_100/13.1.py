import numpy as np
import pandas as pd

from data import df

index = 'f'

# if isinstance(index, int):
#     df['age'].iloc[[index]] += 1
# else:
#     df['age'].loc[[index]] += 1

df['age'][index] += 1

print(df)
