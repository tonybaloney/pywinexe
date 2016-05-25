from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '1.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pywinexe',
    version=__version__,
    description='A Python wrapper client for the winexe utility',
    long_description=long_description,
    url='https://github.com/tonybaloney/pywinexe',
    download_url='https://github.com/tonybaloney/pywinexe/tarball/' + __version__,
    license='APACHE2',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 2',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Anthony Shaw',
    author_email='anthony.shaw@dimensiondata.com',
    test_suite="tests",
)