#!/usr/bin/env python
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from maskurl import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()

download_url = 'https://github.com/RedXBeard/RomanNumbers/tarball/%s'%__version__
setup(
    name='django_maskurl',
    packages = ['django_maskurl'],
    version = __version__,
    description = 'To mask django url paths, instead of built in template tag',
    author = u"Barbaros YILDIRIM",
    author_email = "barbarosaliyildirim@gmail.com",
    url = "http://redxbeard.github.io/django_maskurl",
    download_url = download_url,
    keywords = ['mask url', 'mask', 'django url mask', 'hide url',
                'hide django url', 'url', 'django url'],
    long_description = long_description,
    classifiers = [
        'Intended Audience :: Python Django Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating Systems :: OS Independent',
        'Programming Language :: Python 2.7 / 2.6',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
