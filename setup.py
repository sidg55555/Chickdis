from setuptools import setup, find_packages

setup(
    name="Chickdis",
    version="0.0.1",
    author="Sidharth Goel",
    author_email="sidharthgoel55555@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    )