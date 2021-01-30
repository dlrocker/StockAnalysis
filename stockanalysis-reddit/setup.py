from setuptools import setup, find_namespace_packages
from os import path
from io import open

script_directory = path.abspath(path.dirname(__file__))

with open(path.join(script_directory, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setup(
    name="stockanalysis-reddit",
    version="1.0.0",
    description="Python package used to pull stock information from Reddit and prepare it for down stream usage",
    long_description=readme,
    long_description_content_type="test/markdown",
    url="",
    author="David Rocker",
    author_email="",
    classifiers=[
        "Private :: Do not upload to pypi server"
    ],
    keywords="Stock Analysis",
    packages=find_namespace_packages(include=["stockanalysis.*"], exclude=["tests"]),
    python_requires=">=3.7",
    install_requires=[],
    # entry_points={
    #    "console_scripts": ["stockanalysis=stockanalysis:main"]
    # },
    project_url={
        "Bug Reports": "https://github.com/dlrocker/StockAnalysis",
        "Support": "https://github.com/dlrocker/StockAnalysis"
    }
)
