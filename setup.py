#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
django-sitewidgets
"""

VERSION = __import__('sitewidgets').VERSION

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires = [
#   'simplejson',
]

#try:
#    __import__('uuid')
#except ImportError:
#    # uuid ensures compatibility with older versions of Python
#    install_requires.append('uuid')

#tests_require = [
   #'logbook',
   #'nose',
   #'unittest2',
#]

setup(
    name='sitewidgets',
    version=VERSION,
    author='Maxime Haineault',
    author_email='max@motion-m.ca',
    url='https://github.com/h3/django-sitewidgets',
    description = 'Reusable site widgets for django',
    long_description=__doc__,
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    license='BSD',
    install_requires=install_requires,
    dependency_links=[],
   #tests_require=tests_require,
   #extras_require={'test': tests_require},
   #test_suite='nose.collector',
    include_package_data=True,
#   entry_points = {
#       'console_scripts': [
#           'duke = bin.client:main',
#       ],
#   },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)



