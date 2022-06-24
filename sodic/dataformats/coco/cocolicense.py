from dataclasses import dataclass, field


@dataclass
class CocoLicense:
    """Represents a hard coded coco license."""

    id: int = field(init=False, default=0)
    name: str = field(init=False, default="")
    url: str = field(init=False, default="")
