from setuptools import setup
import os

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="markdownify-notion",
    description="A small package to markdownify notion blocks.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Sergio Sanchez",
    url="https://github.com/chekos/markdownify-notion",
    project_urls={
        "Issues": "https://github.com/chekos/markdownify-notion/issues",
        "CI": "https://github.com/chekos/markdownify-notion/actions",
        "Changelog": "https://github.com/chekos/markdownify-notion/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["markdownify_notion"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
)
