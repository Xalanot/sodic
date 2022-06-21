from typing import List

from PIL import Image, ImageDraw

from sodic.drawables import Drawable


class SodicImage:
    """Image class containing the different drawable objects in a scene.

    Args:
        width: Height of the image in pixel.
        height: Width of the image in pixel.
        drawables: Drawables representing the objects in the scene.
    """

    def __init__(self, width: int, height: int, drawables: List[Drawable]) -> None:
        self.width = width
        self.height = height
        self.drawables = drawables

    def draw(self) -> Image.Image:
        """Draws the image on a white background."""
        image = Image.new("RGB", (self.width, self.height), color=(255, 255, 255))
        image_draw = ImageDraw.Draw(image)
        for drawable in self.drawables:
            drawable.draw(image_draw)
        return image
