from setuptools import setup
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='get_nba_data',
      version='1.0.0',
      description='easy tool to load nba data with',
      url='http://github.com/jkim65537/get_nba_data',
      author='Jun Kim',
      author_email='jkim65537@gmail.com',
      long_description=long_description,
      license='MIT',
      packages=['get_nba_data'],
      download_url = 'https://github.com/jkim65537/get_nba_data/dist/get_nba_data-1.0.0.tar.gz',
      install_requires=['requests', 'pandas'],
      zip_safe=False)
