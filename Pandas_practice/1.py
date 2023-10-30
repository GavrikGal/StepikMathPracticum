import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('torg.csv', sep=';')

print(df.head(7))
print()
print(df.describe())
print()
print(df[['CP_QUANTITY', 'IP_PROP30']].groupby('IP_PROP30').sum())
print('----'*10)
df2 = df[['IP_PROP32', 'CP_QUANTITY']].groupby('IP_PROP32').sum()
print(df2.sort_values('CP_QUANTITY'))
