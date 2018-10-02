from setuptools import setup


def readme():
	with open('README.rst') as f:
		return f.read()


setup(name='jk_treetaggerwrapper',
	version='0.2018.9.26',
	description='This python module provides a wrapper around `treetaggerwrapper` which in turn is a Python based wrapper around the `TreeTagger` PoS-tagger.',
	author='Jürgen Knauth',
	author_email='pubsrc@binary-overflow.de',
	license='Apache 2.0',
	url='https://github.com/jkpubsrc/python-module-jk-treetaggerwrapper',
	download_url='https://github.com/jkpubsrc/python-module-jk-treetaggerwrapper/tarball/0.2018.9.26',
	keywords=[
		"treetagger",
		"pos-tagging"
	],
	packages=[
		"jk_treetaggerwrapper",
	],
	install_requires=[
		"treetaggerwrapper",
		"jk_utils",
	],
	include_package_data=True,
	classifiers=[
		'Development Status :: 4 - Beta',
		'Programming Language :: Python :: 3.5',
		'License :: OSI Approved :: Apache Software License'
	],
	long_description=readme(),
	zip_safe=False)












