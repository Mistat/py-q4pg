# -*- coding: utf-8 -*-
from distutils.core import setup, Extension

requires = [
    'psycopg2>=2.4',
    ]

setup(
    name = 'py-q4pg',
    py_modules = ['q4pg'],
    version = '0.0.1',
    description = 'A simple message queue using PostgreSQL in Python.',
    author='Shin Aoyama',
    author_email = "smihica@gmail.com",
    url = "https://github.com/smihica/py-q4pg",
    download_url = "",
    keywords = ["db", "queue", "psql"],
    requires = ['psycopg2'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment"
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = """\
A simple message queue using PostgreSQL in Python.
""",
    )
