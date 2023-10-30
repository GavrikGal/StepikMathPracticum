import numpy as np
from data import df


colums = list(df.columns[(df.dtypes == np.int64) | (df.dtypes == np.float64)])

for colum in colums:
    print(f'{colum}:{df[colum].sum()}')
