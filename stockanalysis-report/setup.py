from setuptools import setup, find_namespace_packages
from os import path
from io import open

script_directory = path.abspath(path.dirname(__file__))

with open(path.join(script_directory, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setup(
    name="stockanalysis-report",
    version="1.0.0",
    description="Python package used to pull stock information from Yahoo Finance generate reports",
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
    install_requires=[
        "yfinance==0.1.55",
        "plotly>=4.14.3",
        "numpy==1.18.1",
        "pandas==0.24.2",
        "flask==1.1.1",
        "flask-cors==3.0.10",
        "connexion==2.7.0",
        "connexion[swagger-ui]"
    ],
    # entry_points={
    #    "console_scripts": ["stockanalysis=stockanalysis:main"]
    # },
    project_url={
        "Bug Reports": "https://github.com/dlrocker/StockAnalysis",
        "Support": "https://github.com/dlrocker/StockAnalysis"
    }
)
