from abc import ABC, abstractmethod

from PIL import ImageDraw


class Drawable(ABC):
    """Abstract base class for drawable objects."""

    @abstractmethod
    def draw(self, image: ImageDraw.Draw):
        """Draws itself on an image."""
        pass
