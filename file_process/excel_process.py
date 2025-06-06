import math

import pandas as pd


class Excel_process:

    def __init__(self, file_xls):
        self.df = None
        self.conditions = {}
        self.file_xls = file_xls

    def read_xls(self):
        df = pd.read_excel(self.file_xls.path, header=None)
        rows = df.values.tolist()
        x = [val for val in rows[0][1:] if not math.isnan(val)]
        y = [val for val in rows[1][1:] if not math.isnan(val)]
        x, y = zip(*sorted(zip(x, y)))
        big_x = [val for val in rows[2][1:] if not math.isnan(val)]
        big_x.sort()
        res = {
            'x_name': rows[0][0],
            'func_name': rows[1][0],
            'x_val': list(x),
            'func_val': list(y),
            'var_name': rows[2][0],
            'func_var': f'f({rows[2][0]})',
            'var_val': big_x,
        }
        res['fuc_var_val'] = [None for _ in range(len(res['var_val']))]
        self.conditions = res
        return res

    def read_xls_diff(self):
        df = pd.read_excel(self.file_xls.path, header=None)
        # self.sort_df(df)
        # self.df = df
        rows = df.values.tolist()
        x = [val for val in rows[0][1:] if not math.isnan(val)]
        y = [val for val in rows[1][1:] if not math.isnan(val)]
        big_x = [val for val in rows[2][1:] if not math.isnan(val)]
        x, y, big_x = zip(*sorted(zip(x, y, big_x)))

        res = {
            'x_name': rows[0][0],
            'func_name': rows[1][0],
            'x_val': list(x),
            'func_val': list(y),
            'analytics_name': f"{rows[1][0]}' analytics",
            'numeric_name': f"{rows[1][0]}' numeric",
            'analytics_val': big_x,
        }
        res['numeric_val'] = [None for _ in range(len(res['analytics_val']))]
        self.conditions = res
        return res
