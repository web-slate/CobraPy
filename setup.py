from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("math_operations.py"),
)
