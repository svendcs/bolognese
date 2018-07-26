# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='bolognese',
    version='0.9.0',
    description='Command line tool for tracking macro nutrients.',
    long_description=long_description,
    url='https://github.com/svendcsvendsen/bolognese',
    author='Svend Christian Svendsen',
    author_email='svendcsvendsen@gmail.com',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',

        'Intended Audience :: End Users/Desktop',

        'Topic :: Utilities',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='iifym dieting macros macronutrients calories kilojoule',

    packages=('bolognese', 'bolognese.core', 'bolognese.commands', 'bolognese.databases'),
    install_requires=['pyyaml'],

    extras_require={  # Optional
        'dev': [],
        'test': [],
    },

    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[('my_data', ['data/data_file'])],  # Optional

    entry_points={
        'console_scripts': [
            'bolognese=bolognese:main',
        ],
    },
)
