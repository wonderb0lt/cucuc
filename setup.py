from setuptools import setup, find_packages

setup(
  name='cucuc',
  version='0.0.1',
  packages=['cucuc'],
  entry_points={
    'console_scripts': {
      'cucucx = cucuc.main:main'
    }
  }
)
