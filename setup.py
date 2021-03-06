#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'jenkins-job-builder==2.0.0.0b1',
    'jinja2==2.9.5',

    # The following is necessary to avoid shitty package dependency conflicts
    # in jenkins-job-builder:
    'pbr>=1.0.0,<2.0',
    'stevedore==1.20.0',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='jankman',
    version='0.1.0',
    description="Command line wrapper around Jenkins Job Builder 2.x+ library.",
    long_description=readme + '\n\n' + history,
    author="Wayne Warren",
    author_email='waynr+jankman@sdf.org',
    url='https://github.com/waynr/jankman',
    packages=[
        'jankman',
    ],
    package_dir={'jankman':
                 'jankman'},
    entry_points={
        'console_scripts': [
            'jankman=jankman.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='jankman',
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
