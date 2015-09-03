#!/usr/bin/env python

import os
import sys
import re

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

version = ''
with open('awesojson/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

packages = ['awesojson']
requires = []

setup(
    name='awesojson',
    version=version,
    description='JSON serialisation/deserialisation Python lib for complex types.',
    long_description=readme,
    author='Vincent Philippon',
    author_email='vince.philippon+python-awesojson@gmail.com',
    url='https://github.com/vphilippon/python-awesojson',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'awesojson': 'awesojson'},
    include_package_data=True,
    install_requires=requires,
    license='LGPL V3.0',
    zip_safe=True,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),
)
