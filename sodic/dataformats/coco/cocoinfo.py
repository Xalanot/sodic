from dataclasses import dataclass, field


@dataclass
class CocoInfo:
    """Represents a hard coded coco info."""

    year: int = field(init=False, default=2022)
    version: str = field(init=False, default="")
    description: str = field(init=False, default="")
    contributor: str = field(init=False, default="")
    url: str = field(init=False, default="")
    date_created: str = field(init=False, default="")
