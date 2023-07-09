
if __name__ == "__main__":
    import numpy as np
    from interp.interp3d.interp_3d import Interp3D
    from interp.interp2d.interp_2d import Interp2D 
    from interp.interp1d.interp_1d import Interp1D
    x = np.linspace(0,2.5,100)
    y = np.linspace(-1,.5,50)
    z = np.linspace(5,25,125)

    X,Y,Z = np.meshgrid(x,y,z,indexing='ij')
    arr = X+2*Y-3*Z

    interp = Interp3D(arr, x,y,z)

    from scipy.interpolate import RegularGridInterpolator
    interp_si = RegularGridInterpolator((x,y,z),arr)

    x0, y0, z0 = (1.1,0.25, 7.5)
    print('this class {}'.format(interp((x0,y0,z0))))
    print('scipy.interpolate.RegularGridInterpolator() {}'.format(interp_si((x0,y0,z0)), x0+2*y0-3*z0))
    print('exact {}'.format(x0+2*y0-3*z0))
    
    
    x = np.linspace(0,2.5,100)
    y = np.linspace(-1,.5,50)

    X,Y = np.meshgrid(x,y,indexing='ij')
    arr = X+2*Y

    interp = Interp2D(arr, x,y)

    from scipy.interpolate import RegularGridInterpolator
    interp_si = RegularGridInterpolator((x,y),arr)
    for i in range(100):
        x0 = np.random.uniform(0,2.5)
        y0 = np.random.uniform(-1,.5)
        # print('this class {}'.format(interp((x0,y0))))
        # print('scipy.interpolate.RegularGridInterpolator() {}'.format(interp_si((x0,y0)), x0+2*y0))
        # print('exact {}'.format(x0+2*y0))
        val = interp((x0,y0))
        si = interp_si((x0,y0))
        assert np.isclose(val, si), f" {val} != {si}"