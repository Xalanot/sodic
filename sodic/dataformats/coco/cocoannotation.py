from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Dict, List, Type

from sodic.drawables import Drawable


@dataclass
class CocoAnnotation:
    """Represents an image entry in the COCO annotations json."""

    segmentation: List[List[float]]
    area: float
    bbox: List[float]
    image_id: int
    id: int
    category_id: int

    @classmethod
    def FromDrawable(
        cls: Type[CocoAnnotation],
        drawable: Drawable,
        category_list: List[str],
        image_id: int,
        id: int,
    ) -> CocoAnnotation:
        """Creates an CocoImage from an SodicImage plus the additional informations.

        Args:
            drawable: The Drawable where the segmentation, area and bbox are extracted.
            category_list: List of names of the categories used as reference for the category_id.
            image_id: Id of the image the annotation belongs to.
            id: Unique id for the COCO annotation.
        Returns:
            The coco annotation.
        """
        segmentation = [drawable.segmentation.outline]
        area = drawable.area
        bbox = [
            drawable.bbox.x,
            drawable.bbox.y,
            drawable.bbox.height,
            drawable.bbox.width,
        ]
        category_id = category_list.index(drawable.category)
        return cls(
            segmentation=segmentation,
            area=area,
            bbox=bbox,
            image_id=image_id,
            id=id,
            category_id=category_id,
        )

    def to_json(self) -> Dict:
        """Returns the dataclass as a json dict in the correct coco format."""
        return asdict(self)
