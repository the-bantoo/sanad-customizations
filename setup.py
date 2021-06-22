# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in sanad_customisations/__init__.py
from sanad_customisations import __version__ as version

setup(
	name='sanad_customisations',
	version=version,
	description='Custom Portals',
	author='Bantoo Accounting Innovations',
	author_email='technical@thebantoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
