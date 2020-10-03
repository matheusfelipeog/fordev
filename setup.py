# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from fordev.__about__ import __version__

from fordev.__about__ import __author__
from fordev.__about__ import __email__


with open('README.md', mode='r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='fordev',
    version=__version__,
    description='Gere, valide e manipule dados randômicos com fordev',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License',
    author=__author__,
    author_email=__email__,
    url='https://github.com/matheusfelipeog/fordev',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    zip_safe=False,
    python_requires='>=3.6',
    project_urls={
        "Bug Tracker": "https://github.com/matheusfelipeog/fordev/issues",
        "Documentation": "https://github.com/matheusfelipeog/fordev/blob/master/doc/README.md",
        "Source Code": "https://github.com/matheusfelipeog/fordev",
    },
    keywords=[
        'fordev', '4dev', '4devs', '4devs-api', '4devs-module', 
        'fourthdev', 'python', 'api', 'scraping', 'data-generator',
        'fake-data', 'fake-data-generator', 'data-manipulation',
        'data-validation', 'random-data'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
