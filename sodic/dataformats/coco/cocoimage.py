from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Dict, Type

from sodic.image import SodicImage


@dataclass
class CocoImage:
    """Represents an image entry in the COCO annotations json."""

    file_name: str
    height: int
    width: int
    id: int
    license: int = field(init=False, default=0)

    @classmethod
    def FromSodicImage(
        cls: Type[CocoImage], sodic_image: SodicImage, file_name: str, id: int
    ) -> CocoImage:
        """Creates an CocoImage from an SodicImage plus the additional informations.

        Args:
            sodic_image: The SodicImage where the height and width are extracted.
            file_name: File name to the saved sodic_image.
            id: Unique id for the COCO annotation.
        """
        return cls(
            file_name=file_name,
            height=sodic_image.height,
            width=sodic_image.width,
            id=id,
        )

    def to_json(self) -> Dict:
        """Returns the dataclass as a json dict in the correct coco format."""
        return asdict(self)
