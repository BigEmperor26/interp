from distutils.core import setup
from Cython.Build import cythonize

from distutils.extension import Extension

import numpy as np

setup(
    name="interp",
    version="0.2.0",
    ext_modules=cythonize(
        [
            "interp/interp3d/interp3d.pyx",
            "interp/interp2d/interp2d.pyx",
            "interp/interp1d/interp1d.pyx",
        ]
    ),
    packages=[
        "interp",
    ],
    include_dirs=[np.get_include()],
)
