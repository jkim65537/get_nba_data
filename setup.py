from setuptools import setup

setup(name='get_nba_data',
      version='0.1',
      description='easy tool to load nba data',
      url='http://github.com/jkim65537/get_nba_data',
      author='Jun Kim',
      author_email='jkim65537@gmail.com',
      license='jkim65537',
      packages=['get_nba_data'],
      install_requires=['requests', 'pandas'],
      zip_safe=False)
