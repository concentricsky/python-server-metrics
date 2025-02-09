# -*- encoding: utf-8 -*-
"""
Python setup file for the server_metrics app.

In order to register your app at pypi.python.org, create an account at
pypi.python.org and login, then register your new app like so:

    python setup.py register

If your name is still free, you can now make your first release but first you
should check if you are uploading the correct files:

    python setup.py sdist

Inspect the output thoroughly. There shouldn't be any temp files and if your
app includes staticfiles or templates, make sure that they appear in the list.
If something is wrong, you need to edit MANIFEST.in and run the command again.

If all looks good, you can make your first release:

    python setup.py sdist upload

For new releases, you need to bump the version number in
server_metrics/__init__.py and re-run the above command.

For more information on creating source distributions, see
http://docs.python.org/2/distutils/sourcedist.html

"""
import os
from setuptools import setup, find_packages
import server_metrics as app


install_requires = [
    'psutil',
]


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name="python-server-metrics",
    version=app.__version__,
    description='A very simple set of methods to collect metrics about your servers',
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='python, utility, metrics',
    author='Martin Brochhaus',
    author_email='mbrochh@gmail.com',
    url="https://github.com/bitmazk/python-server-metrics",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
)
