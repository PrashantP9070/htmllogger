from setuptools import setup, Extension ,find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="htmllogger",
    version="0.1",
    author = "Prashant Pawar",
    author_email="prashantpawar7090@gmail.com",
    description="Python library provides interactive test report for selenium automation project",
    license="MIT",
    keywords="selenium, page object model, pom, pages, page factory, htmllogger, html report, logger",
    install_requires=['selenium'],
    url="https://github.com/PrashantP9070/htmllogger",
    packages=find_packages(),
    long_description = long_description,
    long_description_content_type='text/markdown'
)
