from typing import Dict

import numpy as np
import pandas as pd

data = input()
# data = '1 1 1'
# data = '1 2 3'


class DataSet:
    def __init__(self, data: str):
        self.data = np.array(data.split(), dtype=int)
        self.mean = round(self.data.mean(), 1)
        self.median = round(np.median(self.data), 1)
        self.modes = pd.Series(self.data).mode().values
        self.stats = self.get_all_stats()

    def show_mean(self):
        print(f'Среднее: {self.mean}')

    def show_median(self):
        print(f'Медиана: {self.median}')

    def show_modes(self):
        modes = list(map(str, self.modes.tolist()))
        modes = ' '.join(modes)
        if len(self.modes) > 1:
            print(f'Моды: {modes}')
        else:
            print(f'Мода: {modes}')

    @staticmethod
    def get_stats(args: Dict[str, object]):
        keys = list(args.keys())
        values = list(args.values())
        stats = []
        funcs = {'=': np.equal, '>': np.greater, '<': np.less}
        for symbol, func in funcs.items():
            if func(values[0], values[1]).any():
                stats.append(f'{keys[0]}{symbol}{keys[1]}')
        return stats

    def get_all_stats(self):
        arg_set = [{'Мо': self.modes, 'Ме': self.median},
                   {'Мо': self.modes, 'Ср': self.mean},
                   {'Ме': self.median, 'Ср': self.mean}]
        stats = []
        for args in arg_set:
            stats.extend(self.get_stats(args))
        return stats

    def show_stats(self):
        for stat in self.stats:
            print(stat)


data_set = DataSet(data)
data_set.show_mean()
data_set.show_median()
data_set.show_modes()
data_set.show_stats()

