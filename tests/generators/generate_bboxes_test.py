from typing import List, Tuple
from unittest.mock import Mock, patch

import numpy as np
import pytest

from sodic.drawables.annotations import BoundingBox
from sodic.generators.generatebboxes import (
    generate_random_bboxes_in_image,
    overlap_between_bboxes_exists,
    sample_image_bbox_sizes,
    sample_n_image_bbox_sizes,
    sort_rectangle_sizes_from_large_to_small,
)
from sodic.generators.specifications import (
    ImageBoundingBoxGenerationSpecification,
)


@pytest.mark.parametrize(
    "image_bbox_spec,expected_image_bbox_sizes",
    [
        (
            ImageBoundingBoxGenerationSpecification(
                [(40, 40), (20, 20)], (0.1, 0.1), 1
            ),
            [(42.3, 39.8), (23.7, 22.0)],
        )
    ],
)
@patch("sodic.generators.generatebboxes.np.random.normal")
def test_sample_image_bbox_sizes(
    mock_random_normal: Mock,
    image_bbox_spec: ImageBoundingBoxGenerationSpecification,
    expected_image_bbox_sizes: List[Tuple[float, float]],
):
    mock_random_normal.side_effect = [
        side_length
        for expected_bbox_size in expected_image_bbox_sizes
        for side_length in expected_bbox_size
    ]

    image_bbox_sizes = sample_image_bbox_sizes(image_bbox_spec)

    assert image_bbox_sizes == expected_image_bbox_sizes


@pytest.mark.parametrize(
    "bbox_specs,expected_bbox_sizes",
    [
        (
            [
                ImageBoundingBoxGenerationSpecification([(40, 40)], (0.0, 0.0), 4),
                ImageBoundingBoxGenerationSpecification([(20, 20)], (0.0, 0.0), 2),
                ImageBoundingBoxGenerationSpecification([(10, 10)], (0.0, 0.0), 1),
            ],
            [[(40, 40)], [(20, 20)], [(40, 40)], [(40, 40)], [(40, 40)]],
        )
    ],
)
def test_sample_bbox_sizes(
    bbox_specs: List[ImageBoundingBoxGenerationSpecification],
    expected_bbox_sizes: List[List[Tuple[float, float]]],
):
    np.random.seed(1)
    bbox_sizes = sample_n_image_bbox_sizes(5, bbox_specs)

    assert bbox_sizes == expected_bbox_sizes


@pytest.mark.parametrize(
    "bbox_a,bbox_b,expected_overlap_exists",
    [
        (BoundingBox(10, 10, 50, 50), BoundingBox(20, 20, 40, 40), True),
        (BoundingBox(10, 10, 50, 50), BoundingBox(70, 10, 20, 20), False),
    ],
)
def test_overlap_between_bboxes_exists(
    bbox_a: BoundingBox, bbox_b: BoundingBox, expected_overlap_exists: bool
) -> None:
    overlap_exists = overlap_between_bboxes_exists(bbox_a, bbox_b)

    assert overlap_exists == expected_overlap_exists


@pytest.mark.parametrize(
    "rectangle_sizes,expected_sorted_rectangle_sizes",
    [
        (
            [(10.2, 20.1), (15.5, 15.9), (100.0, 100.5)],
            [(100.0, 100.5), (15.5, 15.9), (10.2, 20.1)],
        )
    ],
)
def test_sort_rectangle_sizes(
    rectangle_sizes: List[Tuple[float, float]],
    expected_sorted_rectangle_sizes: List[Tuple[float, float]],
):
    sorted_rectangle_sizes = sort_rectangle_sizes_from_large_to_small(rectangle_sizes)

    assert expected_sorted_rectangle_sizes == sorted_rectangle_sizes


@pytest.mark.parametrize(
    "image_shape,rectangle_sizes",
    [
        ((100, 100), [(10, 10), (20, 20)]),
        ((100, 100), [(60, 60), (20, 20), (20, 20)]),
    ],
)
def test_generate_random_bboxes_in_image_random_test(
    image_shape: Tuple[int, int], rectangle_sizes: List[Tuple[float, float]]
):
    bboxes = generate_random_bboxes_in_image(image_shape, rectangle_sizes)

    assert len(bboxes) == len(rectangle_sizes)

    for i, bbox_a in enumerate(bboxes[:-1]):
        for bbox_b in bboxes[i + 1 :]:
            assert not overlap_between_bboxes_exists(bbox_a, bbox_b)

    for rectangle_size in rectangle_sizes:
        correct_bbox_found = False
        for bbox in bboxes:
            if bbox.width == rectangle_size[0] and bbox.height == rectangle_size[1]:
                correct_bbox_found = True
                break
        assert correct_bbox_found


@patch("sodic.generators.generatebboxes.np.random.uniform")
def test_generate_random_bboxes_in_image_with_overlapping_bboxes(
    mock_start_position: Mock,
):
    image_shape = (100, 100)
    rectangle_sizes = [(10.0, 10.0), (80.0, 80.0)]
    mock_start_position.side_effect = [5, 5, 50, 50, 88, 88]

    bboxes = generate_random_bboxes_in_image(image_shape, rectangle_sizes)

    expected_bboxes = [BoundingBox(5, 5, 80, 80), BoundingBox(88, 88, 10, 10)]
    assert expected_bboxes == bboxes


@patch("sodic.generators.generatebboxes.np.random.uniform")
def test_generate_random_bboxes_image_raises_error_if_no_bbox_can_be_found(
    mock_start_position: Mock,
):
    image_shape = (100, 100)
    rectangle_sizes = [(10.0, 10.0), (80.0, 80.0)]
    mock_start_position.side_effect = [5, 5, 50, 50, 25, 30, 40, 32, 88, 88]
    maximum_samples_to_draw = 3

    with pytest.raises(RuntimeError):
        generate_random_bboxes_in_image(
            image_shape, rectangle_sizes, maximum_samples_to_draw
        )
