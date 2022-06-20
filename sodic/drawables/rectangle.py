from dataclasses import dataclass

from PIL import ImageDraw

from .drawable import Drawable


@dataclass
class Rectangle(Drawable):
    """Object representing a rectangle."""
    x1: float
    y1: float
    x2: float
    y2: float
    color: str

    def draw(self, image: ImageDraw) -> None:
        """Draws itself on an image."""
        image.polygon(xy=[
            (self.x1, self.y1), 
            (self.x2, self.y1),
            (self.x2, self.y2),
            (self.x1, self.y2)
        ], fill=self.color)