#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
 
import linuxB2git
 

setup(
 
    # le nom de la bibliothèque, tel qu'il apparaitre sur pypi
    name='linuxB2git',
 
    # la version du code
    version=linuxB2git.__version__,
    
    # find_packages() de setuptools qui va cherche tous les packages
    # python recursivement dans le dossier courant.
    
    packages=find_packages(),
 
    author="PE et Mel",
 
    author_email="lemail@gmail.com",
 
    description="Chat à distance",
 
    long_description=open('README.md').read(),
 
    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,
 
    url='http://github.com/Mel2p/ScriptFilRouge',
 
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Communications",
    ],
 
    license="WTFPL",
 
)
