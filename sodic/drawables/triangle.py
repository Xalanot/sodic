from dataclasses import dataclass
import math

from PIL import ImageDraw

from .annotations import BoundingBox, Segmentation
from .drawable import Drawable


@dataclass
class Triangle(Drawable):
    """Object representing a triangle."""

    x1: float
    y1: float
    x2: float
    y2: float
    x3: float
    y3: float
    color: str = "red"

    def draw(self, image: ImageDraw) -> None:
        """Draws itself on an image."""
        image.polygon(
            xy=[
                (self.x1, self.y1),
                (self.x2, self.y2),
                (self.x3, self.y3),
            ],
            fill=self.color,
        )

    @property
    def segmentation(self) -> Segmentation:
        """Calculates the segmentation outline in the format [x1,y1,x2,y2,...]."""
        return Segmentation(
            outline=[
                self.x1,
                self.y1,
                self.x2,
                self.y2,
                self.x3,
                self.y3,
            ]
        )

    @property
    def area(self) -> float:
        """Calculates the area of the segmentation mask in pixel^2.

        For the calculation heron's formula is used where a, b, c are the length of the sides
        of the triangle and s is half the perimeter.
        """

        def calculate_length(x1: float, y1: float, x2: float, y2: float):
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        a = calculate_length(self.x1, self.y1, self.x2, self.y2)
        b = calculate_length(self.x2, self.y2, self.x3, self.y3)
        c = calculate_length(self.x1, self.y1, self.x3, self.y3)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    @property
    def bbox(self) -> BoundingBox:
        """Calculates the bouding box of the segmentation."""
        min_x = min(self.x1, self.x2, self.x3)
        min_y = min(self.y1, self.y2, self.y3)
        max_x = max(self.x1, self.x2, self.x3)
        max_y = max(self.y1, self.y2, self.y3)
        return BoundingBox(
            x=min_x, y=min_y, width=(max_x - min_x), height=(max_y - min_y)
        )
