#!/usr/bin/python

import sys, os

from setuptools import setup, find_packages

__author__ = 'Luis C. Cruz <carlitos.kyo@gmail.com>'
__version__ = '1.0.2'


# Setuptools version
SETUPTOOLS_METADATA = dict(
    install_requires = ['setuptools', 'simplejson', 'oauth'],
    include_package_data = True,
    
)


def read_file(name):
    return open(os.path.join(os.path.dirname(__file__),
                             name)).read()

readme = read_file('README.txt')

setup(name='turboengine',
      version=__version__,
      description="Utilities for google app engine",
      long_description='\n\n'.join([readme]),
      classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: Internet',
        ],
      package_dir={'': 'src'},
      packages=find_packages('src'),
      keywords='GAE utility',
      author='Luis C. Cruz',
      author_email='carlitos.kyo@gmail.com',
      url='https://github.com/carlitux/turboengine',
      license='MIT',
      zip_safe=True,
      )



