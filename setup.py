import setuptools
#!/usr/bin/env python3

from setuptools import setup

setup(name='agr-datafile-manager',
      version='0.0.1',
      description='Alliance datafile manager package',
      url='',
      author='Alliance',
      author_email='help@alliancegenome.org',
      packages=['agr-datafile-manager'],
      install_requires=[
          'namedlist',
          'inflect',
          'PyYAML',
          'numpy',
          'urllib3',
          'ontobio
	]
      zip_safe=False)
