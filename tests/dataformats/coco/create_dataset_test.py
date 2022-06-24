import pathlib
import tempfile

from sodic.dataformats.coco.createdataset import (
    create_coco_directory_structure,
    draw_image_to_disk,
)
from sodic.drawables import Rectangle
from sodic.image import SodicImage


def test_creation_of_coco_directories():
    temp_dir = tempfile.TemporaryDirectory()
    coco_path = pathlib.Path(temp_dir.name, "path/to/coco")

    create_coco_directory_structure(coco_path)

    assert coco_path.is_dir()
    assert (coco_path / "images").is_dir()
    assert (coco_path / "annotations").is_dir()


def test_save_image_to_disk():
    temp_dir = tempfile.TemporaryDirectory()
    export_path = pathlib.Path(temp_dir.name, "image.png")
    sodic_image = SodicImage(
        width=100, height=100, drawables=[Rectangle(10, 10, 60, 60)]
    )

    draw_image_to_disk(sodic_image, export_path)

    assert export_path.is_file()
