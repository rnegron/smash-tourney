import os
import sys
from shutil import rmtree

from setuptools import Command, setup

VERSION = "0.2.0"

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="smash-tourney",
    version=VERSION,
    description='The Open Source Super Smash Bros. 1v1 randomizer with customizable "versus" voice implementer!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Raúl Negrón",
    author_email="raul@raulnegron.me",
    python_requires=">=3.6.0",
    url="https://github.com/rnegron/smash-tourney",
    py_modules=["smash_tourney.smash_tourney"],
    entry_points={
        "console_scripts": ["smash-tourney=smash_tourney.smash_tourney:main"]
    },
    install_requires=["pydub", "gTTS"],
    extras_require=None,
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Topic :: Games/Entertainment",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
