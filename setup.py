from Cython.Build import cythonize
# cython:
# distutils: extra_compile_args = -O3
from setuptools import setup
setup(
    ext_modules = cythonize("cython_code.pyx", annotate=True)
)