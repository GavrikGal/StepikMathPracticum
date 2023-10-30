from data import df


column = 'animal'
old_value = 'snake'
new_value = 'python'

df[column] = df[column].replace(old_value, new_value)

print(df)