#!/usr/bin/env python3

"""Project testing."""

import subprocess  # noqa: S404
import sys


def run_pytest() -> None:
    """Execute pytest on the project."""
    print("Running pytest ...")
    returncode = subprocess.call(  # noqa: S607, S603
        [
            "pytest",
            "--junitxml=report.xml",
            "--cov=diecastingcreator/",
            # "--cov-report=xml:coverage.xml",
            "--cov-report=xml",
            "--cov-report=html",
            # "--cov-report=term-missing",
            "tests",
        ]
    )
    if returncode != 0:
        sys.exit(returncode)


def main():
    run_pytest()


if __name__ == "__main__":
    main()
