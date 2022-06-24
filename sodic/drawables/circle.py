from dataclasses import dataclass
import math
from typing import Tuple

import numpy as np
from PIL import ImageDraw

from .annotations import BoundingBox, Segmentation
from .drawable import Drawable


@dataclass
class Circle(Drawable):
    """Object representing a circle.

    Args:
        x: x-coordinate of middle point the circle.
        y: y-coordinate of middle point the circle.
        radius: Radius of the circle.
        color: Color of the circle.
    """

    x: float
    y: float
    radius: float
    color: str = "red"

    def calculate_upper_left_corner(self) -> Tuple[float, float]:
        """Calculates the upper left point of a circle based on the middlepoint and the radius."""
        x1 = self.x - self.radius
        y1 = self.y - self.radius
        return x1, y1

    def calculate_lower_right_corner(self) -> Tuple[float, float]:
        """Calculates the lower right point of a circle based on the middlepoint and the radius."""
        x2 = self.x + self.radius
        y2 = self.y + self.radius
        return x2, y2

    def draw(self, image: ImageDraw) -> None:
        """Draws itself on an image."""
        upper_left_corner = self.calculate_upper_left_corner()
        lower_right_corner = self.calculate_lower_right_corner()
        image.ellipse(xy=[upper_left_corner, lower_right_corner], fill=self.color)

    @property
    def category(self) -> str:
        """Returns the name of the category this object belongs."""
        return "circle"

    @property
    def segmentation(self) -> Segmentation:
        """Calculates the segmentation outline in the format [x1,y1,x2,y2,...].

        It samples the outline of the circle with angle steps of 0.1.
        """
        outline = []
        for angle in np.linspace(0, 2 * math.pi, 1000):
            x_sample = self.x + math.cos(angle) * self.radius
            y_sample = self.y - math.sin(angle) * self.radius
            outline += [x_sample, y_sample]
        return Segmentation(outline=outline)

    @property
    def area(self) -> float:
        """Calculates the area of the segmentation mask in pixel^2."""
        return math.pi * self.radius**2

    @property
    def bbox(self) -> BoundingBox:
        """Calculates the bouding box of the segmentation."""
        x1, y1 = self.calculate_upper_left_corner()
        x2, y2 = self.calculate_lower_right_corner()
        return BoundingBox(x=x1, y=y1, width=(x2 - x1), height=(y2 - y1))
