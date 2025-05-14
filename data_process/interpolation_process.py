from copy import copy


class Interpolation_process:
    def __init__(self, data):
        self.data = data
        self.x: list = data['x_val']
        self.y: list = data['func_val']
        self.x_name = data['x_name']
        self.y_name = data['func_name']
        self.X: list = data['var_val']
        self.Y: list = data['fuc_var_val']
        self.x_name = data['var_name']
        self.y_name = data['func_var']

    def process_lagrange(self):
        self.Y.clear()
        for j in range(len(self.X)):
            res = 0
            for i in range(len(self.x)):
                res += self.process_lagr_monomial(self.X[j], i)
            self.Y.append(res)
        self.data['fuc_var_val'] = self.Y

    def process_lagr_monomial(self, big_x: float, ind: int):
        numerator = 1
        denominator = 1
        up = copy(self.x)
        minuend = up.pop(ind)
        for i in range(len(up)):
            numerator *= (big_x - up[i])
            denominator *= (minuend - up[i])
        return self.y[ind] * numerator / denominator

    def process_newton(self):
        self.Y.clear()
        f = [self.y] + [[] for _ in range(len(self.y) - 1)]
        self.find_f(self.x, f)
        f = [val[0] for val in f]
        for val in self.X:
            self.process_newton_monomial(f, val)
        self.data['fuc_var_val'] = self.Y

    def find_f(self, x: list, f: list[list], i=1):
        if i == len(f):
            return
        for k in range(len(f) - i):
            f[i].append((f[i - 1][k + 1] - f[i - 1][k]) / (x[k + i] - x[k]))
        self.find_f(x, f, i + 1)

    def process_newton_monomial(self, f: list, big_x):
        res = f[0]
        for i in range(1, len(f)):
            k = f[i]
            for j in range(i):
                k *= (big_x - self.x[j])
            res += k
        self.Y.append(res)
