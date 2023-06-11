#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='pyProcNetDev',
    version='0.0.1',
    url='https://github.com/SpareSimian/pyProcNetDev',
    download_url='https://github.com/SpareSimian/pyProcNetDev/archive/master.zip',
    author='SpareSimian',
    author_email='SpareSimian+github@SewingWitch.com',
    license='Apache v2.0 License',
    packages=['pyProcNetDev'],
    description='A pythonic library to parse /proc/net/dev',
    long_description = open('README.md','r').read(),
    keywords=['interface', 'system information', 'network', '/proc'],
)
