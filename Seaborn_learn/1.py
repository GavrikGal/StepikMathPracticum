import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

matplotlib.get_backend()
matplotlib.use('TkAgg')

sns.set()
df = pd.read_csv('tips.csv')
print(df.head(5))

# sns.displot(df['total_bill'])

# sns.jointplot(x='total_bill', y='tip', data=df)

# sns.kdeplot(df['total_bill'])
# sns.rugplot(df['total_bill'])

# sns.pairplot(df)

# sns.pairplot(df, hue='sex', palette='Set1')

# fig = sns.PairGrid(df)
# fig.map_diag(plt.hist)
# fig.map_upper(plt.scatter)
# fig.map_lower(sns.kdeplot)

# fig = sns.FacetGrid(df, col='time', row='smoker')
# fig = fig.map(plt.hist, 'total_bill')

# sns.countplot(x='day', data=df)

# sns.barplot(x='sex', y='total_bill', data=df)

# sns.boxplot(x='day', y='total_bill', data=df, palette='Set1')

# sns.boxplot(x='day', y='tip', data=df, hue='smoker', palette='Set1')

# sns.violinplot(x='day', y='total_bill', data=df, palette='Set2')

# sns.violinplot(x='day', y='total_bill', data=df, hue='smoker')

# sns.stripplot(x="day", y="total_bill", data=df, palette="Set2")

# sns.swarmplot(x='day', y='total_bill', hue='sex', data=df)

# sns.catplot(x='total_bill', y='sex', data=df, kind='bar')

cor_df = df.corr(numeric_only=True)
print(cor_df)

# sns.heatmap(cor_df, annot=True, cmap='coolwarm')

fig, ax = plt.subplots(figsize=(8, 6))
sns.regplot(x='total_bill', y='tip', data=df, ax=ax)
ax.set_title('График распределения двух признаков')
plt.xlabel('Сумма чека')
plt.ylabel('Чаевые')
fig.savefig('filename.png', dpi=150)
plt.show()

