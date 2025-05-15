class Differentiation_process:
    def __init__(self, data):
        self.data = data
        self.x: list = data['x_val']
        self.y: list = data['func_val']
        self.x_name = data['x_name']
        self.y_name = data['func_name']
        self.analytics_val: list = data['analytics_val']
        self.numeric_val: list = data['numeric_val']
        self.analytics_name = data['analytics_name']
        self.numeric_name = data['numeric_name']
        self.h = self.x[1] - self.x[0]

    def get_interp_differential(self):
        res = []
        for i in range(2, len(self.y) - 2):
            res.append((1 * self.y[i - 2] - 8 * self.y[i - 1] + 8 * self.y[i + 1] - 1 * self.y[i + 2]) / (12 * self.h))
        self.numeric_val = self.interp_first() + res + self.interp_last()
        self.data['numeric_val'] = self.numeric_val
        self.data['numeric_name'] = "f'(x) interpolation"

    def interp_first(self):
        return [
            (-25 * self.y[0] + 48 * self.y[1] - 36 * self.y[2] + 16 * self.y[3] - 3 * self.y[4]) / (12 * self.h),
            (-3 * self.y[0] - 10 * self.y[1] + 18 * self.y[2] - 6 * self.y[3] + 1 * self.y[4]) / (12 * self.h)
        ]

    def interp_last(self):
        return [
            (-1 * self.y[-5] + 6 * self.y[-4] - 18 * self.y[-3] + 10 * self.y[-2] + 3 * self.y[-1]) / (12 * self.h),
            (3 * self.y[-5] - 16 * self.y[-4] + 36 * self.y[-3] - 48 * self.y[-2] + 25 * self.y[-1]) / (12 * self.h)
        ]

    def get_approximation_differential(self):
        res = []
        for i in range(2, len(self.y) - 2):
            res.append(
                (-14 * self.y[i - 2] - 7 * self.y[i - 1] + 7 * self.y[i + 1] + 14 * self.y[i + 2]) / (70 * self.h)
            )
        self.numeric_val = self.approximation_first() + res + self.approximation_last()
        self.data['numeric_val'] = self.numeric_val
        self.data['numeric_name'] = "f'(x) approximation"

    def approximation_first(self):
        return [
            (-54 * self.y[0] + 13 * self.y[1] + 40 * self.y[2] + 27 * self.y[3] - 26 * self.y[4]) / (70 * self.h),
            (-34 * self.y[0] + 3 * self.y[1] + 20 * self.y[2] + 17 * self.y[3] - 6 * self.y[4]) / (70 * self.h)
        ]

    def approximation_last(self):
        return [
            (6 * self.y[-5] - 17 * self.y[-4] - 20 * self.y[-3] - 3 * self.y[-2] + 34 * self.y[-1]) / (70 * self.h),
            (26 * self.y[-5] - 27 * self.y[-4] - 40 * self.y[-3] - 13 * self.y[-2] + 54 * self.y[-1]) / (70 * self.h)
        ]
