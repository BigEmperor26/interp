A faster 1-2-3D interpolation to replace `scipy.interpolate.RegularGridInterpolator()`

Implemented after <https://stackoverflow.com/questions/41220617/python-3d-interpolation-speedup>.

Installation (requires **cython**):

```
python3 setup.py install
```

Usage:

```

if __name__ == "__main__":
    import numpy as np
    from interp.interp3d.interp_3d import Interp3D
    from interp.interp2d.interp_2d import Interp2D 
    from interp.interp1d.interp_1d import Interp1D
    import time
    from scipy.interpolate import RegularGridInterpolator
    
    x = np.linspace(0,2.5,100)
    y = np.linspace(-1,.5,50)
    z = np.linspace(5,25,125)

    X,Y,Z = np.meshgrid(x,y,z,indexing='ij')
    arr = X+2*Y-3*Z

    interp = Interp3D(arr, x,y,z)

    interp_si = RegularGridInterpolator((x,y,z),arr)

    x0, y0, z0 = (1.1,0.25, 7.5)
    time_3d = time.time()
    value_3d = interp((x0,y0,z0))
    took_3d = time.time() - time_3d
    print (f'this 3d interpolation took {took_3d} seconds, value is {value_3d}')
    time_si = time.time()
    value_si = interp_si((x0,y0,z0))
    took_si = time.time() - time_si
    print (f'scipy.interpolate.RegularGridInterpolator() took {took_si} seconds, value is {value_si}')
    print('exact {}'.format(x0+2*y0-3*z0))
    
    
    x = np.linspace(0,2.5,100)
    y = np.linspace(-1,.5,50)

    X,Y = np.meshgrid(x,y,indexing='ij')
    arr = X+2*Y

    interp = Interp2D(arr, x,y)

    interp_si = RegularGridInterpolator((x,y),arr)

    x0, y0 = (1.1,0.25)
    time_2d = time.time()
    value_2d = interp((x0,y0))
    took_2d = time.time() - time_2d
    print (f'this 2d interpolation took {took_2d} seconds, value is {value_2d}')
    time_si = time.time()
    value_si = interp_si((x0,y0))
    took_si = time.time() - time_si
    print (f'scipy.interpolate.RegularGridInterpolator() took {took_si} seconds, value is {value_si}')
    print('exact {}'.format(x0+2*y0))
    
    x = np.linspace(0,2.5,100)
    X, = np.meshgrid(x,indexing='ij')
    arr = X*2
    # import pdb; pdb.set_trace()
    interp = Interp1D(arr, x)
    
    # interp_si = RegularGridInterpolator((x,),arr)
    
    x0 = 1.1
    time_1d = time.time()
    value_1d = interp((x0))
    took_1d = time.time() - time_1d
    print (f'this 1d interpolation took {took_1d} seconds, value is {value_1d}')
    # time_si = time.time()
    # value_si = interp_si((x0))
    # took_si = time.time() - time_si
    # print (f'scipy.interpolate.RegularGridInterpolator() took {took_si} seconds, value is {value_si}')
    print ('exact {}'.format(x0*2))
```
