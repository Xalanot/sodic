import copy
from typing import List, Tuple

import numpy as np

from sodic.drawables.annotations import BoundingBox
from sodic.generators.calculate_probability_bins import (
    calculate_probability_bins,
)
from sodic.generators.specifications import (
    ImageBoundingBoxGenerationSpecification,
)


def sample_image_bbox_sizes(
    image_bbox_spec: ImageBoundingBoxGenerationSpecification,
) -> List[Tuple[float, float]]:
    """Samples random bbox sizes based on given bbox specification for an´single image.

    Note: This only samples the width and the height of the bboxes.

    Args:
        image_bbox_spec: Specification for the bboxes in a single image.
    Returns:
        List of bbox sizes (width, height).
    """
    bbox_sizes = []
    for recatanlge_size in image_bbox_spec.bbox_sizes:
        bbox_width = float(
            np.random.normal(
                loc=recatanlge_size[0],
                scale=image_bbox_spec.deviations_in_percent[0] * recatanlge_size[0],
            )
        )
        bbox_height = float(
            np.random.normal(
                loc=recatanlge_size[1],
                scale=image_bbox_spec.deviations_in_percent[1] * recatanlge_size[1],
            )
        )
        bbox_sizes.append((bbox_width, bbox_height))
    return bbox_sizes


def sample_n_image_bbox_sizes(
    number_of_samples: int, bbox_specs: List[ImageBoundingBoxGenerationSpecification]
) -> List[List[Tuple[float, float]]]:
    """Random sample n bounding box specs to generate bounding box sizes for individual images.

    Args:
        number_of_samples: Number of samples (images) to generate.
        bbox_specs: List of bounding box spec to sample from.
    Returns:
        A list of images with their related bouding box sizes.
    """
    probability_weights = [bbox_spec.probability_weight for bbox_spec in bbox_specs]
    probability_bins = calculate_probability_bins(probability_weights)
    random_number_for_each_sample = np.random.uniform(size=(number_of_samples))
    sample_indices = np.digitize(random_number_for_each_sample, probability_bins)
    sampled_bbox_sizes = list()
    for index in sample_indices:
        bbox_spec = bbox_specs[index]
        sampled_bbox_sizes.append(sample_image_bbox_sizes(bbox_spec))
    return sampled_bbox_sizes


def overlap_between_bboxes_exists(bbox_a: BoundingBox, bbox_b: BoundingBox) -> bool:
    """Calculates if an overlap (intersection) between two bouding boxes exists.

    Args:
        bbox_a: First bouding box to compare.
        bbox_b: Second bounding box to compare.
    Returns:
        True, if overlap (intersection) exists.
    """
    x_overlap = (bbox_a.x + bbox_a.width) >= bbox_b.x and (
        bbox_b.x + bbox_b.width
    ) >= bbox_a.x
    y_overlap = (bbox_a.y + bbox_a.height) >= bbox_b.y and (
        bbox_b.y + bbox_b.height
    ) >= bbox_a.y
    return x_overlap and y_overlap


def sort_rectangle_sizes_from_large_to_small(
    rectangle_sizes: List[Tuple[float, float]]
) -> List[Tuple[float, float]]:
    """Sorts a list of rectangle sizes based on the area of the rectangle in descending order.

    Args:
        rectanlge_sizes: List of rectangle sizes to sort.
    Returns:
        A sorted list of rectangle sizes.
    """
    copied_rectangle_sizes = copy.deepcopy(rectangle_sizes)
    copied_rectangle_sizes.sort(key=lambda x: x[0] * x[1], reverse=True)
    return copied_rectangle_sizes


def generate_random_bboxes_in_image(
    image_shape: Tuple[int, int],
    rectangle_sizes: List[Tuple[float, float]],
    maximum_samples_to_draw: int = 100,
) -> List[BoundingBox]:
    """Generate random bounding boxes in a image.

    Note: Only the start position of the bounding boxes are generated in this function. The bouding box
    sizes have to be passed in as a sorted list from large to small. The function will start with drawing
    random start positions starting with the largest bouding box. Each new drawn bounding box is
    compared with the already existing ones to check if there is any overlap. If there is an overlap the
    bbox is rejected and a new one is drawn. This process will be repeated until maximum_samples_to_draw
    tries are made, where then a runtime exception is thrown.

    Args:
        image_shape: Shape of the image to generate.
        rectangle_sizes: Sorted list of rectangle sizes defining the sizes
        of the boundign boxes to generate.
        maximum_samples_to_draw: Maximum tries for generating a single bounding box
        until a runtime exception is thrown.
    Returns:
        A list of bounding boxes for a single image.
    """
    sorted_rectangle_sizes = sort_rectangle_sizes_from_large_to_small(rectangle_sizes)

    bboxes: List[BoundingBox] = list()
    for rectangle_size in sorted_rectangle_sizes:
        max_possible_start_x = image_shape[0] - rectangle_size[0] - 1
        max_possible_start_y = image_shape[1] - rectangle_size[1] - 1
        for _ in range(maximum_samples_to_draw):
            start_x = np.random.uniform(0, max_possible_start_x)
            start_y = np.random.uniform(0, max_possible_start_y)
            bbox_proposal = BoundingBox(
                start_x, start_y, rectangle_size[0], rectangle_size[1]
            )

            overlap_exists = False
            for bbox in bboxes:
                if overlap_between_bboxes_exists(bbox_proposal, bbox):
                    overlap_exists = True
                    break
            if overlap_exists:
                continue
            else:
                bboxes.append(bbox_proposal)
                break

    if len(bboxes) < len(rectangle_sizes):
        raise RuntimeError(
            f"""Found no matching bboxes for specified image shape ({image_shape}) \
                 and rectangle sizes({rectangle_sizes})"""
        )

    return bboxes
