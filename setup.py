from distutils.core import setup
from Cython.Build import cythonize

from distutils.extension import Extension

import numpy as np

setup(
    name="interp",
    ext_modules=cythonize(
      ["interp3d/interp3d.pyx",
                          "interp2d/interp2d.pyx"]),
      
    packages=[
          "interp3d",
            "interp2d"
            ],
    include_dirs=[np.get_include()],
)