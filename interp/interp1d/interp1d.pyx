cimport numpy as np
import numpy as np
from libc.math cimport floor
from cython cimport boundscheck, wraparound, nonecheck, cdivision

@cdivision(True)
cpdef np.float_t _interp1D(np.float_t[::1] v, np.float_t x, int X):

    cdef:
        int i, x0, x1
        np.float_t xd
        np.float_t *v_c

    v_c = &v[0]

    x0 = <int>floor(x)
    x1 = x0 + 1

    xd = (x-x0)/(x1-x0)

    if x0 >= 0  and x1 < X :
        c = v_c[x0]*(1-xd) + v_c[x1]*xd

    else:
        c = 0

    return c
