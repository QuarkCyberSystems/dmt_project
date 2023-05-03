from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in flats/__init__.py
from flats import __version__ as version

setup(
	name="flats",
	version=version,
	description="Flats",
	author="qcs",
	author_email="hiran@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
