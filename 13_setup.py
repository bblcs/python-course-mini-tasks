from distutils.core import setup, Extension

module = Extension("foreign", sources=["13.c"])

setup(
    ext_modules=[module],
)
