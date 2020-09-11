#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 11-09-2020 12:50:56

    [Description]
"""
__author__ = "Benedict Wilkins"
__email__ = "benrjw@gmail.com"
__status__ = "Development"
from setuptools import setup, find_packages

setup(name='gym_epong',
      version='0.0.1',
      description='An efficient implementation of pong for gym.',
      url='https://github.com/BenedictWilkinsAI/gym-epong',
      author='Benedict Wilkins',
      author_email='brjw@hotmail.co.uk',
      license='GNU3',
      classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
      ],
      install_requires=['gym', 'numpy'],
      packages=find_packages())
