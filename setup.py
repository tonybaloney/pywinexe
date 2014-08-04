#!/usr/bin/env python
# -*- coding: utf-8 -*-

import winexe

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# if sys.argv[-1] == 'publish':
#     os.system('python setup.py sdist upload')
#     sys.exit()

packages = [
    'winexe',
]

with open('README.md') as f:
    readme = f.read()

setup(
    name='winexe',
    version=winexe.__version__,
    description='Python bindings for winexe.',
    long_description=readme,
    author=u'Jakob Aarøe Dam',
    author_email='jakob.a.dam@gmail.com',
    url='http://github.com/jakobadam/python-winexe',
    packages=packages,
    package_dir={'winexe': 'winexe'},
    include_package_data=True,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python'
    ),
)
