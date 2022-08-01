from typing import List

import pytest

from sodic.generators.calculate_probability_bins import (
    calculate_probability_bins,
)


@pytest.mark.parametrize(
    "probability_weights,expected_probability_bins",
    [
        (
            [1, 1],
            [0.5, 1],
        ),
        (
            [4, 2, 1],
            [4 / 7, 6 / 7, 1],
        ),
    ],
)
def test_calculate_probability_bins(
    probability_weights: List[float],
    expected_probability_bins: List[float],
):
    probability_bins = calculate_probability_bins(probability_weights)

    assert probability_bins == expected_probability_bins
