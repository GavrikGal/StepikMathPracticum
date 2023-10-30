import numpy as np
import pandas as pd

from data import df

age_between = [2, 4]

print(df[df['age'].between(*age_between)])