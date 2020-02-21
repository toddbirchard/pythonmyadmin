"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pythonmyadmin',
    version='0.0.1',
    description='Lightweight GUI for modifying database tables.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/toddbirchard/pythonmyadmin',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='Lightweight Database GUI',
    packages=find_packages(),
    install_requires=['Flask',
                      'Flask-SQLAlchemy',
                      'Pandas',
                      'PyMySQL',
                      'Flask-assets',
                      'Dash',
                      'Dash_core_components',
                      'Dash_html_components',
                      'Dash-renderer',
                      'Wtforms',
                      'Redis',
                      'Python-dotenv'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'run = wsgi:__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/toddbirchard/pythonmyadmin/issues',
        'Source': 'https://github.com/toddbirchard/pythonmyadmin/',
    },
)
