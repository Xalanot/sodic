import numpy as np

from sodic.drawables import Circle, Rectangle, Triangle
from sodic.drawables.annotations import BoundingBox
from sodic.drawables.drawable import Drawable
from sodic.generators.specifications import (
    ImageDrawbaleGenerationSpecification,
)


def generate_rectangle_in_bbox(bbox: BoundingBox, color: str) -> Rectangle:
    """Generates a drawable of type rectangle in a bounding box.

    Args:
        bbox: Bounding box in which the rectangle has to be generated.
        color: Color of the rectangle to generate.
    Returns:
        The generated rectangle.
    """
    rectangle = Rectangle(
        bbox.x, bbox.y, bbox.x + bbox.width, bbox.y + bbox.height, color
    )
    return rectangle


def generate_circle_in_bbox(bbox: BoundingBox, color: str) -> Circle:
    """Generates a drawable of type circle in a bounding box.

    If the bouding box is not a square, the smaller side length is used
    as diameter of the circle.

    Args:
        bbox: Bounding box in which the circle has to be generated.
        color: Color of the circle to generate.
    Returns:
        The generated circle.
    """
    min_side = min(bbox.width, bbox.height)
    circle = Circle(bbox.x + min_side / 2, bbox.y + min_side / 2, min_side / 2, color)
    return circle


def generate_triangle_in_bbox(bbox: BoundingBox, color: str) -> Triangle:
    """Generates a drawable of type triangle in a bounding box.

    The triangle fills the lower part of a rectangle divided by a diagonal
    from the top left corner to the bottom right corner.

    Args:
        bbox: Bounding box in which the triangle has to be generated.
        color: Color of the triangle to generate.
    Returns:
        The generated triangle.
    """
    triangle = Triangle(
        bbox.x,
        bbox.y,
        bbox.x + bbox.width,
        bbox.y + bbox.height,
        bbox.x,
        bbox.y + bbox.height,
        color,
    )
    return triangle


def generate_drawable_in_bbox(
    drawable_spec: ImageDrawbaleGenerationSpecification, bbox: BoundingBox
) -> Drawable:
    """Generates a drawable defined in drawable spec in a bouding box.

    This function works as a kind of factory function supporting multiple
    different drawables.

    Args:
        drawable_spec: Specification of the drawable to generate.
        bbox: Bounding box in which the drawable has to be generated.
    Returns:
        The generated drawable.
    """
    drawable_to_draw = drawable_spec.drawable
    color = np.random.choice(drawable_spec.colors)
    if drawable_to_draw == "rectangle":
        return generate_rectangle_in_bbox(bbox, color)
    elif drawable_to_draw == "circle":
        return generate_circle_in_bbox(bbox, color)
    else:
        return generate_triangle_in_bbox(bbox, color)
