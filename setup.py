# coding=utf-8
"""
Setup for scikit-surgery
"""

from setuptools import setup, find_packages
import versioneer

# Get the long description
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='scikit-surgery',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='scikit-surgery',
    long_description=long_description,
    url='https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/scikit-surgery',
    author='Thomas Dowrick',
    author_email='YOUR-EMAIL@ucl.ac.uk',
    license='BSD-3 license',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',


        'License :: OSI Approved :: BSD License',


        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],

    keywords='medical imaging',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
        ]
    ),

    install_requires=[
        'six>=1.10',
        'numpy>=1.11',
        'pillow',
    ],

    entry_points={
        'console_scripts': [
            'sksurgery=sksurgery.__main__:main',
        ],
    },
)
