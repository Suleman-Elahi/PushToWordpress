#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '0.15'

# Grab requirments.

with open('require.txt','r') as f:
    required = f.readlines()



# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

if sys.argv[-1] == 'test_upload':
    os.system('python setup.py upload -r https://testpypi.python.org/pypi')

with open('README.md', 'r') as f:
    long_desc = f.read()

setup(
    name = "Push_To_Wordpress",
    version = VERSION,
    #scripts = ['presser.py'],

    install_requires = required,

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.md', '*.rst','*.txt','*.ini'],
    },
    packages = ['push_to_wordpress',],
    entry_points = {
        'console_scripts': [
            'presser = push_to_wordpress.presser:presser'
        ],
    },
    # metadata for upload to PyPI
    author = "Alonisser",
    author_email = "alonisser@gmail.com",
    description = "a commandline tool to post to Markdown files to wordpress posts (based on wordpress XML-RPC)",
    long_description = long_desc,
    license = "OSI Approved :: MIT License",
    keywords = "blogging wordpress commandline",
    url = "https://github.com/alonisser/PushToWordpress",   # project home page, if any
    classifiers=(
        'Development Status :: 3 - Beta',
        'Environment :: Console',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7', #maybe more, didn't check
        'Topic :: Internet :: WWW/HTTP :: Site Management'

    ),

    # could also include long_description, download_url, classifiers, etc.
)
