from dataclasses import asdict, dataclass, field
from typing import List

from .cocoannotation import CocoAnnotation
from .cococategory import CocoCategory
from .cocoimage import CocoImage
from .cocoinfo import CocoInfo
from .cocolicense import CocoLicense


@dataclass
class CocoDataFormat:
    """Represents the annotation json for the coco dataset."""

    images: List[CocoImage]
    annotations: List[CocoAnnotation]
    categories: List[CocoCategory]
    info: CocoInfo = field(default_factory=lambda: CocoInfo())
    licenses: List[CocoLicense] = field(default_factory=lambda: [CocoLicense()])

    def to_json(self):
        """Returns the dataclass as a json dict in the correct coco format."""
        return asdict(self)
