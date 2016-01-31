from setuptools import setup, find_packages

setup(
	name='Textmining',
	version='0.0.1',
	description='statistical text mining',
	packages=['textmining', 'textmining/data/*', 'textmining/examples/*'],
	package_data={'': ['*.txt']}
)
