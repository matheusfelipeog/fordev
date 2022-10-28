import os
import sys
from shutil import rmtree
from setuptools import setup, find_packages, Command

from fordev import __version__
from fordev import __author__
from fordev import __email__


here = os.path.abspath(os.path.dirname(__file__))


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish package in Pypi.'
    user_options = []

    @staticmethod
    def print_status(msg):
        """Prints message in bold and yellow."""
        print(f'\033[1;33m{msg}\033[0m')

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.print_status('Removing previous builds…')

            rmtree(os.path.join(here, 'dist'))
            rmtree(os.path.join(here, 'build'))

        except OSError:
            pass

        self.print_status('Build Source and Wheel distribution…')
        os.system(f'{sys.executable} setup.py sdist bdist_wheel')

        self.print_status('Uploading the package to PyPi via Twine…')
        os.system('twine upload --config-file .pypirc --repository pypi dist/*')

        sys.exit()


with open(os.path.join(here, 'README.md'), mode='r', encoding='utf-8') as f:
    long_description = '\n' + f.read()


setup(
    name='fordev',
    version=__version__,
    description='Gere e valide dados randômicos com fordev',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License',
    author=__author__,
    author_email=__email__,
    url='https://github.com/matheusfelipeog/fordev',
    packages=find_packages(
        exclude=('tests',)
    ),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'colorama'
    ],
    zip_safe=False,
    python_requires='>=3.6',
    project_urls={
        "Bug Tracker": "https://github.com/matheusfelipeog/fordev/issues",
        "Documentation": "https://fordev.readthedocs.io/",
        "Source Code": "https://github.com/matheusfelipeog/fordev",
    },
    keywords=[
        'fordev', '4dev', '4devs', '4devs-api', '4devs-module',
        'fourthdev', 'python', 'api', 'scraping', 'data-generator',
        'fake-data', 'fake-data-generator', 'data-manipulation',
        'data-validation', 'random-data'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    # setup.py publish support
    cmdclass={
        'publish': PublishCommand
    }
)
