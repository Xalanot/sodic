#!/usr/bin/env python3

"""Code formatting."""
import subprocess  # noqa: S404
import sys
from typing import List, Tuple

import click
from colorama import Fore, Style
from isort.main import main as isort_main


def run_black(filenames: List[str], check_only: bool = False) -> None:
    """Run black."""
    cmd = (
        ["black", "--diff", "--check"] + filenames
        if check_only
        else ["black"] + filenames
    )
    print(
        Fore.GREEN,
        Style.BRIGHT,
        f"\nRunning {' '.join(cmd)} ...\n",
        Fore.RESET,
        Style.RESET_ALL,
    )
    returncode = subprocess.call(cmd)  # noqa: S603
    if returncode != 0:
        print(f"black exited with returncode {returncode}. Aborting!")
        sys.exit(returncode)


def run_isort(filenames: List[str], check_only: bool = False) -> None:
    """Run isort to sort the imports."""
    args = ["--check-only", "--diff"] + filenames if check_only else filenames
    print(
        Fore.GREEN,
        Style.BRIGHT,
        f"\nRunning isort {' '.join(args)} ...\n",
        Fore.RESET,
        Style.RESET_ALL,
    )
    # this will sys.exit() on error!
    isort_main(args)


@click.command()
@click.argument("filenames", nargs=-1)
def main(filenames: Tuple) -> None:
    FORMATTERS = [run_isort, run_black]
    filenames_list = list(filenames) if len(filenames) > 0 else ["."]
    for formatter in FORMATTERS:
        formatter(filenames=filenames_list)
        sys.stdout.flush()
        sys.stderr.flush()


@click.command()
@click.argument("filenames", nargs=-1)
def main_check(filenames: Tuple) -> None:
    FORMATTERS = [run_isort, run_black]
    filenames_list = list(filenames) if len(filenames) > 0 else ["."]
    for formatter in FORMATTERS:
        formatter(filenames=filenames_list, check_only=True)
        sys.stdout.flush()
        sys.stderr.flush()


if __name__ == "__main__":
    main()
