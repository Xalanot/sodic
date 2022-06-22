from dataclasses import dataclass


@dataclass
class BoundingBox:
    """Class representing a bounding box annotation.

    Args:
        x: x-coordinate of the upper left corner.
        y: y-coordinate of the upper right corner.
        width: Width of the bounding box.
        height: Heiht of the bounding box.
    """

    x: float
    y: float
    width: float
    height: float
