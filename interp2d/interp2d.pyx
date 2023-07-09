cimport numpy as np
import numpy as np
from libc.math cimport floor
from cython cimport boundscheck, wraparound, nonecheck, cdivision

@cdivision(True)
cpdef np.float_t _interp2D(np.float_t[:,::1] v, np.float_t x, np.float_t y, int X, int Y):

    cdef:
        int i, x0, x1, y0, y1, dim
        np.float_t xd, yd, c00, c01, c10, c11, c0, c1, c
        np.float_t *v_c

    v_c = &v[0,0]

    x0 = <int>floor(x)
    x1 = x0 + 1
    y0 = <int>floor(y)
    y1 = y0 + 1

    xd = (x-x0)/(x1-x0)
    yd = (y-y0)/(y1-y0)

    if x0 >= 0 and y0 >= 0 and x1 < X and y1 < Y:
        c00 = v_c[Y*x0+y0]*(1-xd) + v_c[Y*x1+y0]*xd
        c10 = v_c[Y*x0+y1]*(1-xd) + v_c[Y*x1+y1]*xd

        c = c00*(1-yd) + c10*yd

    else:
        c = 0

    return c
