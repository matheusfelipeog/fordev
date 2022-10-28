"""
fordev.utils
------------

This module contains useful classes and functions for the fordev package.
"""

__all__ = ['CheckVersion']

from fordev import __version__
from fordev import __author__
from fordev import __email__

from colorama import init, deinit, Fore

import requests


class CheckVersion(object):
    """Check if package has a newer version."""

    def __init__(self, current_version: str, package_name: str):
        
        self.current_version = current_version
        self.package_name = package_name
        self.latest_version = None
    
    def endpoint(self):
        """Build endpoint of Pypi API."""

        pypi = 'https://pypi.org'
        route = '/pypi/{package}/json'.format(package=self.package_name)

        return pypi + route

    @staticmethod
    def version_to_tuple(version: str, separator='.'):
        """Convert version to tuple. Ex: '1.4.3' to (1, 4, 3)."""

        return tuple(map(int, version.split(separator)))

    def get_latest_version(self):
        try:
            url = self.endpoint()

            r = requests.get(url)
            
            if r.status_code == 200:
                self.latest_version = r.json()['info']['version']

                return self.version_to_tuple(self.latest_version)

        except Exception:
            pass

    def is_newer_version_available(self):
        """Check if latest version is greater than the current version."""

        current_version = self.version_to_tuple(self.current_version)
        latest_version = self.get_latest_version()

        if latest_version > current_version:
            return True
        
        return False

    def print_status(self):
        """Print a warning if of package has a newer version."""

        init()  # Start colorama

        warning = (
            Fore.YELLOW + 'You are using an old version of the {package} package (v{current_version}), '
            'a new version has been released (v{latest_version}).\n'
            'Please run: python -m pip install {package} --upgrade' + Fore.RESET
        ).format(
            package=self.package_name,
            current_version=self.current_version,
            latest_version=self.latest_version
        )

        print(warning)

        deinit()  # Stop colorama
    
    @staticmethod
    def run(current_version: str, package_name: str):
        """Run CheckVersion without instantiating an object."""

        check = CheckVersion(current_version, package_name)

        if check.is_newer_version_available():
            check.print_status()
