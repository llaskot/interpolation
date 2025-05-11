import math

import pandas as pd




class Excel_process:
    def __init__(self, file_xls):
        self.df = None
        self.conditions = None;
        self.file_xls = file_xls

    def read_xls(self):
        df = pd.read_excel(self.file_xls.path, header=None)
        self.sort_df(df)
        self.df = df
        rows = df.values.tolist()
        res = {
            'x_name': rows[0][0],
            'func_name': rows[1][0],
            'x_val': rows[0][1:],
            'func_val': rows[1][1:],
            'var_name': rows[2][0],
            'func_var': f'f({rows[2][0]})',
            'var_val': [val for val in rows[2][1:] if not math.isnan(val) ],
        }
        res['fuc_var_val'] = [None for _ in range(len( res['var_val'] ))]
        self.conditions = res
        print(res)
        return res

    def sort_df(self, df):
        # срез с 0 по 2 (не включительно) строку, с 1-го значения и до конца
        data = df.iloc[0:2, 1:]
        # сортировка по x (первой строке)
        sort_idx = data.iloc[0].argsort()  # индексы отсортированных x-значений
        sorted_data = data.iloc[:, sort_idx.values]  # применяем сортировку к столбцам
        df.iloc[0:2, 1:] = sorted_data  # запихать обратно в фрейм
        df.iloc[2, 1:] = sorted(df.iloc[2, 1:], key=lambda x: (pd.isna(x), x))  # сортировка 3й строки
