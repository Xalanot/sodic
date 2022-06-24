from dataclasses import dataclass, field


@dataclass
class CocoCategory:
    """Represents a coco object detection category."""

    id: int
    name: str
    supercategory: str = field(init=False, default="geometry")
