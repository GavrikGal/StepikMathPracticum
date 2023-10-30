from scipy import stats
import pandas as pd


sample = list(map(int, input().split()))

mode = pd.Series(sample).mode()

print(*mode.values)