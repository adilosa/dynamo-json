from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='dynamo-json',
    version='1.0.0',
    description='Swap between DynamoDB JSON and normal JSON',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/adilosa/dynamo-json',
    author='adilosa',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='dynamo json dynamodb',  # Optional
    py_modules=["dynamo_json", "cli"],
    entry_points={
        'console_scripts': [
            'dynamo-json=cli:dynamo_json'
        ]
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/adilosa/dynamo-json/issues',
        'Say Thanks!': 'http://saythanks.io/to/adilosa',
        'Source': 'https://github.com/adilosa/dynamo-json/',
    },
)