from dataclasses import dataclass
from typing import List


@dataclass
class Segmentation:
    """Class representing a segmentation annotation.

    Args:
        outline: List of outline points in the form [x1, y1, x2, y2, ...]
    """

    outline: List[float]
