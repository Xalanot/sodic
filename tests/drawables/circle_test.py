import pytest

from sodic.drawables import Circle
from sodic.drawables.annotations import BoundingBox


@pytest.mark.parametrize(
    "circle,expected_area",
    [(Circle(50, 50, 20), 1256.637), (Circle(40, 30, 20), 1256.637)],
)
def test_area_calculation(circle: Circle, expected_area: float):
    area = circle.area

    assert area == pytest.approx(expected_area)


@pytest.mark.parametrize(
    "circle,expected_bounding_box",
    [
        (Circle(50, 50, 20), BoundingBox(30, 30, 40, 40)),
        (Circle(45, 27, 10.5), BoundingBox(34.5, 16.5, 21, 21)),
    ],
)
def test_bbox_calculation(circle: Circle, expected_bounding_box: BoundingBox):
    bounding_box = circle.bbox

    assert bounding_box == expected_bounding_box
