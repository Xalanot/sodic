import pytest

from sodic.drawables import Rectangle
from sodic.drawables.annotations import BoundingBox, Segmentation


@pytest.mark.parametrize(
    "rectangle,expected_segmentation",
    [
        (Rectangle(10, 10, 60, 60), Segmentation([10, 10, 60, 10, 60, 60, 10, 60])),
        (
            Rectangle(10.5, 10.5, 20, 20),
            Segmentation([10.5, 10.5, 20, 10.5, 20, 20, 10.5, 20]),
        ),
    ],
)
def test_segmentation_calculation(
    rectangle: Rectangle, expected_segmentation: Segmentation
):
    segmentation = rectangle.segmentation

    assert segmentation == expected_segmentation


@pytest.mark.parametrize(
    "rectangle,expected_area",
    [(Rectangle(10, 10, 60, 60), 2500), (Rectangle(10.5, 10.5, 20, 20), 90.25)],
)
def test_area_calculation(rectangle: Rectangle, expected_area: float):
    area = rectangle.area

    assert area == expected_area


@pytest.mark.parametrize(
    "rectangle,expected_bounding_box",
    [
        (Rectangle(10, 10, 60, 60), BoundingBox(10, 10, 50, 50)),
        (Rectangle(10.5, 10.5, 20, 20), BoundingBox(10.5, 10.5, 9.5, 9.5)),
    ],
)
def test_bbox_calculation(rectangle: Rectangle, expected_bounding_box: BoundingBox):
    bounding_box = rectangle.bbox

    assert bounding_box == expected_bounding_box
