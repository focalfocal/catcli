from setuptools import setup, find_packages
from codecs import open
from os import path
import catcli

readme = 'README.md'
here = path.abspath(path.dirname(__file__))

try:
    from pypandoc import convert_file
    read_readme = lambda f: convert_file(f, 'rst')
except ImportError:
    print('\n[WARNING] pypandoc not found, could not convert \"{}\"\n'.format(readme))
    read_readme = lambda f: open(f, 'r').read()

VERSION = catcli.__version__
REQUIRES_PYTHON = '>=3'

setup(
    name='catcli',
    version=VERSION,

    description='The command line catalog tool for your offline data (added rar support)',
    long_description=read_readme(readme),
    url='https://github.com/focalfocal/catcli',
    download_url = 'https://github.com/focalfocal/catcli/archive/v'+VERSION+'.tar.gz',

    author='deadc0de6 for the catcli, matiasb for python-unrar, and focalfocal for the integration',
    author_email='for main author: deadc0de6@foo.bar',

    license='GPLv3',
    python_requires=REQUIRES_PYTHON,
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          ],

    keywords='catalog commandline indexer offline',
    packages=find_packages(exclude=['tests*']),
    install_requires=['docopt', 'anytree', 'python-rar'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },

    entry_points={
        'console_scripts': [
            'catcli=catcli:main',
        ],
    },
)
