# -*- coding:utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import os

version = '1.5'
description = 'A configurable pipeline, aimed at transforming content for import and export'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = ('\n'.join((
    read('README.rst'), '\n\n',
    read('docs', 'HISTORY.txt'),
)))


setup(
    name='collective.transmogrifier',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 3.3',
        'Framework :: Plone :: 4.0',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='content import filtering',
    author='Jarn',
    author_email='info@jarn.com',
    url='http://pypi.python.org/pypi/collective.transmogrifier',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFCore',
    ],
)
