import numpy as np
import pandas as pd

from data import df


print(df[df['age'].isnull()])