from abc import ABC, abstractmethod

from PIL import ImageDraw

from .annotations import BoundingBox, Segmentation


class Drawable(ABC):
    """Abstract base class for drawable objects."""

    @abstractmethod
    def draw(self, image: ImageDraw.Draw):
        """Draws itself on an image."""
        pass

    @property
    @abstractmethod
    def segmentation(self) -> Segmentation:
        """Calculates the segmentation outline in the format [x1,y1,x2,y2,...]."""
        pass

    @property
    @abstractmethod
    def area(self) -> float:
        """Calculates the area of the segmentation mask in pixel^2."""
        pass

    @property
    @abstractmethod
    def bbox(self) -> BoundingBox:
        """Calculates the bouding box of the segmentation."""
        pass
