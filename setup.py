#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='jenkins_manager',
    version='0.1.0',
    description="Commnad line wrapper around Jenkins Job Builder 2.x+ library.",
    long_description=readme + '\n\n' + history,
    author="Wayne Warren",
    author_email='waynr+jenkins-manager@sdf.org',
    url='https://github.com/waynr/jenkins_manager',
    packages=[
        'jenkins_manager',
    ],
    package_dir={'jenkins_manager':
                 'jenkins_manager'},
    entry_points={
        'console_scripts': [
            'jenkins_manager=jenkins_manager.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='jenkins_manager',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
