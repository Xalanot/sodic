import pytest

from sodic.drawables import Triangle
from sodic.drawables.annotations import BoundingBox, Segmentation


@pytest.mark.parametrize(
    "triangle,expected_segmentation",
    [
        (Triangle(10, 10, 60, 60, 10, 60), Segmentation([10, 10, 60, 60, 10, 60])),
        (Triangle(20, 20, 30, 10, 50, 50), Segmentation([20, 20, 30, 10, 50, 50])),
    ],
)
def test_segmentation_calculation(
    triangle: Triangle, expected_segmentation: Segmentation
):
    segmentation = triangle.segmentation

    assert segmentation == expected_segmentation


@pytest.mark.parametrize(
    "triangle,expected_area",
    [(Triangle(10, 10, 60, 60, 10, 60), 1250), (Triangle(20, 20, 30, 10, 50, 50), 300)],
)
def test_area_calculation(triangle: Triangle, expected_area: float):
    area = triangle.area

    assert area == expected_area


@pytest.mark.parametrize(
    "triangle,expected_bounding_box",
    [
        (Triangle(10, 10, 60, 60, 10, 60), BoundingBox(10, 10, 50, 50)),
        (Triangle(20, 20, 30, 10, 50, 50), BoundingBox(20, 10, 30, 40)),
    ],
)
def test_bbox_calculation(triangle: Triangle, expected_bounding_box: BoundingBox):
    bounding_box = triangle.bbox

    assert bounding_box == expected_bounding_box
