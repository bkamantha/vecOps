from setuptools import setup, find_packages
from os.path import abspath, dirname, join

# Fetches the content from README.md
# This will be used for the "long_description" field.
README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()

# Setup configuration
setup(
    # Name of the project (REQUIRED)
    name="vecops",

    # Version of the project (REQUIRED)
    version="1.0.3",

    # Packages to include (EITHER py_modules OR packages should be present)
    packages=find_packages(exclude="tests"),

    # Short description (OPTIONAL)
    description="A Python library for vector manipulation",

    # Long description from README.md (OPTIONAL)
    long_description=README_MD,

    # Project URL (OPTIONAL)
    # url="",

    # Author information (OPTIONAL)
    author_name="Bhanuka Kamantha",
    # author_email="",

    # Classifiers for categorization (OPTIONAL)
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only"
    ],

    # Keywords for searching (OPTIONAL)
    keywords="vector calculation maths mathematics"
)
