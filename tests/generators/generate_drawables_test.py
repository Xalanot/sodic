import pytest

from sodic.drawables import Circle, Rectangle, Triangle
from sodic.drawables.annotations import BoundingBox
from sodic.generators.generatedrawables import (
    generate_circle_in_bbox,
    generate_rectangle_in_bbox,
    generate_triangle_in_bbox,
)


@pytest.mark.parametrize(
    "bbox,expected_rectangle",
    [
        (BoundingBox(10, 10, 50, 50), Rectangle(10, 10, 60, 60)),
        (BoundingBox(14, 12, 40, 20), Rectangle(14, 12, 54, 32)),
    ],
)
def test_generate_rectangle_in_bbox(bbox: BoundingBox, expected_rectangle: Rectangle):
    rectangle = generate_rectangle_in_bbox(bbox, "red")

    assert rectangle == expected_rectangle


@pytest.mark.parametrize(
    "bbox,expected_circle",
    [
        (BoundingBox(10, 10, 60, 60), Circle(40, 40, 30)),
        (BoundingBox(10, 10, 40, 20), Circle(20, 20, 10)),
    ],
)
def test_generate_circle_in_bbox(bbox: BoundingBox, expected_circle: Circle):
    circle = generate_circle_in_bbox(bbox, "red")

    assert circle == expected_circle


@pytest.mark.parametrize(
    "bbox,expected_triangle",
    [
        (BoundingBox(10, 10, 60, 60), Triangle(10, 10, 70, 70, 10, 70)),
        (BoundingBox(10, 20, 30, 40), Triangle(10, 20, 40, 60, 10, 60)),
    ],
)
def test_generate_triangle_in_bbox(bbox: BoundingBox, expected_triangle: Circle):
    triangle = generate_triangle_in_bbox(bbox, "red")

    assert triangle == expected_triangle
