from .interp1d import _interp1D

class Interp1D(object):
    def __init__(self, v, x):
        self.v = v
        self.min_x, self.max_x = x[0], x[-1]
        self.delta_x = (self.max_x - self.min_x)/(x.shape[0]-1)

    def __call__(self, t):
        X= self.v.shape[0]

        x = (t-self.min_x)/self.delta_x
        return _interp1D(self.v, x, X)