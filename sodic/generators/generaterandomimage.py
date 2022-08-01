from typing import List, Tuple

import numpy as np

from sodic.drawables.annotations import BoundingBox
from sodic.drawables.drawable import Drawable
from sodic.generators.calculate_probability_bins import (
    calculate_probability_bins,
)
from sodic.generators.generatebboxes import (
    generate_random_bboxes_in_image,
    sample_n_image_bbox_sizes,
)
from sodic.generators.generatedrawables import generate_drawable_in_bbox
from sodic.generators.specifications import (
    ImageBoundingBoxGenerationSpecification,
    ImageDrawbaleGenerationSpecification,
)
from sodic.image import SodicImage


def generate_drawables_in_bboxes(
    drawable_specs: List[ImageDrawbaleGenerationSpecification],
    bboxes: List[BoundingBox],
) -> List[Drawable]:
    """Randomly chooses drawables to be generated in bounding boxes.

    Args:
        drawable_specs: List of drawable generation specifications which can be used for generating
        drawables in bounding boxes.
        bboxes: Bounding boxes to be used for generating drawables.
    Returns:
        List of drawables (one for each provided bounding box.
    """
    probability_weights = [
        drawable_spec.probability_weight for drawable_spec in drawable_specs
    ]
    probability_bins = calculate_probability_bins(probability_weights)
    random_number_for_each_bbox = np.random.uniform(size=(len(bboxes)))
    sample_indices = np.digitize(random_number_for_each_bbox, probability_bins)
    drawables = list()
    for index, bbox in zip(sample_indices, bboxes):
        drawable_spec = drawable_specs[index]
        drawable = generate_drawable_in_bbox(drawable_spec, bbox)
        drawables.append(drawable)
    return drawables


def generate_random_images(
    image_shape: Tuple[int, int],
    drawable_specs: List[ImageDrawbaleGenerationSpecification],
    bbox_specs: List[ImageBoundingBoxGenerationSpecification],
    images_to_generate: int,
) -> List[SodicImage]:
    """Generates multiple random sodic images.

    Args:
        image_shape: Shape of the image.
        drawable_specs: List of drawbale specs to randomly choose from.
        bbox_specs: List of bound box specs to randomly choose from
        images_to_generate: Number of images to generate.
    Returns:
        List of generated images.
    """
    bbox_sizes_for_n_images = sample_n_image_bbox_sizes(images_to_generate, bbox_specs)
    images = list()
    for bbox_sizes in bbox_sizes_for_n_images:
        bboxes = generate_random_bboxes_in_image(
            image_shape, rectangle_sizes=bbox_sizes
        )
        drawables = generate_drawables_in_bboxes(drawable_specs, bboxes)
        image = SodicImage(
            width=image_shape[0], height=image_shape[1], drawables=drawables
        )
        images.append(image)
    return images
