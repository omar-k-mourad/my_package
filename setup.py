from setuptools import setup, find_packages

setup(
    name='my_package',
    version = '0.1',
    packages=find_packages(exclude = ['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requries=['numpy'],
    url='', #github
    author='omar mourad',
    author_email='omar.khaledpop@gmail.com'
)