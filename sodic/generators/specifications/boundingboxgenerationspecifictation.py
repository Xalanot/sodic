from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class ImageBoundingBoxGenerationSpecification:
    """Class representing an image bounding box specification used for generation.

    Note: This specification describes bouding box that are used together to form
    objects in a single image.

    Args:
        bbox_sizes: Sizes of the bounding boxes to generate.
        deviations_in_percent: First standard deviation in percent for all bounding box sizes.
        probability_weight: Value to determine the probability that this
        bounding box specification is chosen.
    """

    bbox_sizes: List[Tuple[int, int]]
    deviations_in_percent: Tuple[float, float]
    probability_weight: float
