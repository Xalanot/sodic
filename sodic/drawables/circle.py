from dataclasses import dataclass
from typing import Tuple

from PIL import ImageDraw

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
    color: str

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
