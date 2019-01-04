"""
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

setup(
    name='pyowlet',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.2',

    description='Python client for Owlet monitors',

    # The project's main homepage.
    url='https://github.com/craigjmidwinter/pyowlet',

    # Author details
    author='craigjmidwinter, angel12',
    author_email='craig.j.midwinter@gmail.com',

    # What does your project relate to?
    keywords='owlet baby',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['requests'],
    extras_require={},
)