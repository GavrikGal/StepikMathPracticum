from data import df


column = "priority"

replace_dict = {'yes': True, 1: True, 'no': False, 0: False}

df[column] = df[column].map(replace_dict)

print(df)

