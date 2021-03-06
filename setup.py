import atexit
import os
import sys
import pawk
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info[0] != 3:
    print("PAWK requires Python 3")
    exit(1)


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    with open('README.rst', 'w') as f:
        f.write(long_description)
    atexit.register(lambda: os.unlink('README.rst'))
except (ImportError, OSError):
    print('WARNING: Could not locate pandoc, using Markdown long_description.')
    with open('README.md') as f:
        long_description = f.read()

description = long_description.splitlines()[0].strip()

setup(
    name='pawk',
    url='http://github.com/alecthomas/pawk',
    download_url='http://github.com/alecthomas/pawk',
    version=pawk.__version__,
    description=description,
    long_description=long_description,
    license='PSF',
    platforms=['any'],
    author='Alec Thomas',
    author_email='alec@swapoff.org',
    py_modules=['pawk'],
    scripts=['pawk'],
    )
