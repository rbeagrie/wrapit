# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wrapit',
    version='0.2.0',
    description='A task loader for doit that supports argparse console scripts',
    long_description=long_description,
    url='https://github.com/rbeagrie/wrapit',
    author='Rob Beagrie',
    author_email='rob@beagrie.com',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='doit development console_scripts build_tools',

    packages=['wrapit'],

    install_requires=['doit'],

)
