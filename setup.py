from distutils.core import setup
import os

description = "Edit encrypted files"
long_description = (
    "Edit Encrypted Files (eef) is a command-line tool to edit "
    "encrypted files with GPG using symmetric-key encryption."
)

setup(
    author="Mathieu Larose",
    author_email="mathieu@mathieularose.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Security :: Cryptography",
        "Topic :: Utilities"
    ],
    keywords="gpg",
    license='GPL',
    description=description,
    long_description=long_description,
    name='eef',
    scripts=['eef'],
    url="https://github.com/larose/eef",
    version='0.0',
)
