# Copyright (C) 2020 Łukasz Langa
import sys

from setuptools import setup

assert sys.version_info >= (3, 6, 0), "black requires Python 3.6+"
from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta



setup(
    name="black",
    use_scm_version={
        "write_to": "src/_black_version.py",
        "write_to_template": 'version = "{version}"\n',
    },
    description="Blacker! Denser Black formatting",
    keywords="automation formatter yapf autopep8 pyfmt gofmt rustfmt",
    author="Kyle Lahnakoski",
    author_email="kyle@lahnakoski.com",
    url="https://github.com/psf/black",
    license="MIT",
    py_modules=["_black_version"],
    packages=["blackd", "black", "blib2to3", "blib2to3.pgen2", "black_primer"],
    package_dir={"": "src"},
    package_data={"blib2to3": ["*.txt"], "black": ["py.typed"]},
    python_requires=">=3.6",
    zip_safe=False,
    install_requires=[
        "click>=6.5",
        "attrs>=18.1.0",
        "appdirs",
        "toml>=0.9.4",
        "typed-ast>=1.4.0",
        "regex>=2020.1.8",
        "pathspec>=0.6, <1",
        "dataclasses>=0.6; python_version < '3.7'",
        "typing_extensions>=3.7.4",
        "mypy_extensions>=0.4.3",
    ],
    extras_require={
        "d": ["aiohttp>=3.3.2", "aiohttp-cors"],
        "colorama": ["colorama>=0.4.3"],
    },
    test_suite="tests.test_black",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    entry_points={"console_scripts": [
        "black=black:patched_main",
        "blackd=blackd:patched_main [d]",
        "black-primer=black_primer.cli:main",
    ]},
)
