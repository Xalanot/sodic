from dataclasses import dataclass

from PIL import ImageDraw

from sodic.drawables.annotations import BoundingBox, Segmentation
from .drawable import Drawable


@dataclass
class Rectangle(Drawable):
    """Object representing a rectangle."""

    x1: float
    y1: float
    x2: float
    y2: float
    color: str = "red"

    def draw(self, image: ImageDraw) -> None:
        """Draws itself on an image."""
        image.polygon(
            xy=[
                (self.x1, self.y1),
                (self.x2, self.y1),
                (self.x2, self.y2),
                (self.x1, self.y2),
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
                self.y1,
                self.x2,
                self.y2,
                self.x1,
                self.y2,
            ]
        )

    @property
    def area(self) -> float:
        """Calculates the area of the segmentation mask in pixel^2."""
        return (self.x2 - self.x1) * (self.y2 - self.y1)

    @property
    def bbox(self) -> BoundingBox:
        """Calculates the bouding box of the segmentation."""
        return BoundingBox(
            x=self.x1, y=self.y1, width=(self.x2 - self.x1), height=(self.y2 - self.y1)
        )
