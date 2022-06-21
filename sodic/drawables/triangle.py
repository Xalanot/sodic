from dataclasses import dataclass

from PIL import ImageDraw

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
    color: str

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
