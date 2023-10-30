import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

var_str = ['2 2 2 2 2 2 2 2 2 2 2 2',
           '1 2 3 4 5 6 1 2 3 4 5 6',
           '1 1 1 1 3 3 3 3 5 5 5 5',
           '5 2 6 6 3 6 2 1 4 6 5 1',
           '2 6 6 4 1 6 1 1 6 6 3 2']

variables = [list(map(int, var.split())) for var in var_str]
np_vars = np.array(variables)
var_mean = np_vars.mean(axis=1)
var_median = np.median(np_vars, axis=1)
df_var_mode = pd.DataFrame(np_vars).mode(axis=1).to_numpy()


mo_gr_me = np.any(np.array([df_var_mode.T > var_median]).T, axis=1).flatten()
mo_gr_cp = np.any(np.array([df_var_mode.T > var_mean]).T, axis=1).flatten()
mo_lt_me = np.any(np.array([df_var_mode.T < var_median]).T, axis=1).flatten()
mo_lt_cp = np.any(np.array([df_var_mode.T < var_mean]).T, axis=1).flatten()
mo_eq_me = np.any(np.array([df_var_mode.T == var_median]).T, axis=1).flatten()
mo_eq_cp = np.any(np.array([df_var_mode.T == var_mean]).T, axis=1).flatten()

me_gr_cp = var_median > var_mean
me_lt_cp = var_median < var_mean
me_eq_cp = var_median == var_mean


np_to_df = np.array([mo_gr_me, mo_gr_cp, mo_lt_me,
                     mo_lt_cp, mo_eq_me, mo_eq_cp,
                     me_gr_cp, me_lt_cp, me_eq_cp]).T

df = pd.DataFrame(np_to_df, columns=['Мо>Ме', 'Мо>Ср', 'Мо<Ме',
                                     'Мо<Ср', 'Мо=Ме', 'Мо=Ср',
                                     'Ме>Ср', 'Ме<Ср', 'Ме=Ср'])

# res = pd.concat([df, df_var_mode], axis=1)
df.index = var_str

print(df)