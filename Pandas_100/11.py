import numpy as np
import pandas as pd

from data import df

filter_names = ["animal", "age"]
filter_values = ["cat", 3]


Z = df[(df[filter_names[0]] == filter_values[0]) \
    & (df[filter_names[1]] < filter_values[1])]

print(Z)