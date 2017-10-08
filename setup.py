"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/guidiego/apistar-mongo-generic
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='apistarmongogeneric',
    version='0.1.0',
    description='Exporting default routes for your projects',
    long_description=long_description,
    url='https://github.com/guidiego/apistar-mongo-generic',
    license='MIT',

    author='Guiherme Diego',
    author_email='guidiego.expgames@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],

    keywords='apistar mongo mongoengine generic',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['mongoengine', 'apistar'],
    extras_require={
        'dev': [],
        'test': [],
    },

    entry_points={
        'console_scripts': [
            'genericfy=genericfy:main',
        ],
    },
)
