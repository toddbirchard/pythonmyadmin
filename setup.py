"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pythonmyadmin',  # Required
    version='0.0.1',  # Required
    description='Lightweight GUI for modifying database tables.',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/toddbirchard/pythonmyadmin',  # Optional
    author='Todd Birchard',  # Optional
    author_email='toddbirchard@gmail.com',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Simple Lightweight Database GUI',  # Optional
    packages=find_packages(),  # Required
    install_requires=['flask',
                      'flask_sqlalchemy',
                      'pandas',
                      'psycopg2-binary',
                      'dash',
                      'dash_core_components',
                      'dash_html_components'],  # Optional
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={  # Optional
        'console_scripts': [
            '__main__',
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/toddbirchard/pythonmyadmin/issues',
        'Source': 'https://github.com/toddbirchard/pythonmyadmin/',
    },
)
