from dataclasses import dataclass
from typing import List

from sodic.drawables import Drawable


@dataclass
class ImageDrawbaleGenerationSpecification:
    """Class representing a drawable specification used for generation.

    Args:
        drawbale: The drawable to generate.
        colors: List of colors that the drawable can have.
        probability_weight: Value to determine the probability that this
        drawable specification is chosen.
    """

    drawable: Drawable
    colors: List[str]
    probability_weight: float
