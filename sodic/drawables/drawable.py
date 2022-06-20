from abc import ABC, abstractmethod

from PIL import ImageDraw


class Drawable(ABC):
    @abstractmethod
    def draw(image: ImageDraw.Draw):
        pass
