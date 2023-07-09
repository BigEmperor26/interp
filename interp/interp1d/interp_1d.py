from .interp1d import _interp1D

class Interp1D(object):
    def __init__(self, v, x, y):
        self.v = v
        self.min_x, self.max_x = x[0], x[-1]
        self.min_y, self.max_y = y[0], y[-1]
        self.delta_x = (self.max_x - self.min_x)/(x.shape[0]-1)
        self.delta_y = (self.max_y - self.min_y)/(y.shape[0]-1)

    def __call__(self, t):
        X,Y = self.v.shape[0], self.v.shape[1]

        x = (t[0]-self.min_x)/self.delta_x
        y = (t[1]-self.min_y)/self.delta_y
        return _interp1D(self.v, x, y, X, Y)