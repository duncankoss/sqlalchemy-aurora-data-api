#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="sqlalchemy-serverless-aurora-plugin",
    version="0.2.5",
    url='https://github.com/duncankoss/sqlalchemy-serverless-aurora-plugin',
    license='Apache Software License',
    author='dkoss',
    author_email='',
    description='A fork of sqlalchemy-aurora-data-api',
    long_description=open('README.rst').read(),
    install_requires=[
        'sqlalchemy',
        'serverless-aurora >= 0.2.3'
    ],
    extras_require={
    },
    packages=find_packages(exclude=['test']),
    entry_points={
        'sqlalchemy.dialects': [
            'mysql.auroradataapi = sqlalchemy_serverless_aurora_plugin:AuroraMySQLDataAPIDialect',
            'postgresql.auroradataapi = sqlalchemy_serverless_aurora_plugin:AuroraPostgresDataAPIDialect'
        ]
    },
    platforms=['MacOS X', 'Posix'],
    test_suite='test',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
