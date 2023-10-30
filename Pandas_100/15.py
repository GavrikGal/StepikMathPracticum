import numpy as np
from data import df

group_by = "animal"

print(df.groupby(group_by)['age'].mean())