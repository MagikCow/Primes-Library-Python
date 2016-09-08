from distutils.core import setup

setup(
    name='Prime_Numbers',
    version='1.0',
    author='MagikCow',
    keywords=['primes', 'prime', 'primes python'],
    packages=packages=find_packages(exclude=['']),
    url='https://github.com/MagikCow/Primes-Library-Python',
    license='LICENSE.txt',
    description='A module adding various prime number functions into python.',
    long_description=open('README.MD').read(),
)
