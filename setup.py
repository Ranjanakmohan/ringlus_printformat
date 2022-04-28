from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ringlus_printformat/__init__.py
from ringlus_printformat import __version__ as version

setup(
	name="ringlus_printformat",
	version=version,
	description="print format",
	author="momscode",
	author_email="infor@momscode.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
