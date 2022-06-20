#!/usr/bin/env python3

"""Project linting."""

import sys
from typing import List, Tuple

import click
import flake8.main.application as flake
from mypy.main import main as mypy


def run_flake8(filenames: List[str]) -> bool:
    """Execute flake8 linter on the project (or file).

    Returns whether there was an error.
    """
    print("Running flake8 ...")
    app = flake.Application()
    app.run(filenames)
    return bool(app.result_count > 0)


def run_mypy(filenames: List[str]) -> bool:
    """Execute type checking on the project (or file).

    Returns whether there was an error.
    """
    print("Running mypy ...")
    try:
        mypy(
            None,
            sys.stdout,
            sys.stderr,
            filenames + ["--color-output"],
            clean_exit=True,
        )
    except SystemExit as e:
        return e.code != 0
    return False


@click.command()
@click.argument("filenames", nargs=-1)
def main(filenames: Tuple) -> None:
    LINTERS = {"flake8": run_flake8, "mypy": run_mypy}
    errors = {}
    filenames_list = list(filenames) if len(filenames) > 0 else ["."]
    for linter_name, linter_func in LINTERS.items():
        linter_error = linter_func(filenames=filenames_list)
        errors[linter_name] = linter_error
        sys.stdout.flush()
        sys.stderr.flush()

    if any(errors.values()):
        print("Exiting due to previous errors")
        for k, v in errors.items():
            status = "error" if v else "no error"
            print(f"  linter '{k}' reports {status}")
        sys.exit(1)


if __name__ == "__main__":
    main()
