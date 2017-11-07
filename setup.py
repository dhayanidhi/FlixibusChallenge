import inspect
import os
import platform
from setuptools import setup, find_packages

py_major_version, py_minor_version, _ = (int(v.rstrip('+')) for v in platform.python_version_tuple())

__location__ = os.path.join(os.getcwd(), os.path.dirname(inspect.getfile(inspect.currentframe())))

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='coding-challange',

    version='0.1',

    description='Coding challange',

    author='challange',

    packages=find_packages(exclude=['build', 'dist', 'tests', '.cache']),

    extras_require={
        'dev': ['check-manifest'],
        'test': [
            'coverage',
            'unittest2',
            'mock',
        ],
    },

    package_data={},

    data_files=[],

    install_requires=[
        'flask'
    ],

    entry_points='''
        [console_scripts]
        modelservice=bin.service:main
    ''',

    scripts=[],

    dependency_links=[],

    zip_safe=False
)