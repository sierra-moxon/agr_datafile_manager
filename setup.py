from setuptools import find_packages
#!/usr/bin/env python3

from setuptools import setup

setup(name='agr-datafile-manager',
      version='0.0.1',
      description='Alliance datafile manager package',
      url='',
      author='Alliance',
      author_email='help@alliancegenome.org',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      zip_safe=False)
