import json
import pathlib
from typing import List

from sodic.image import SodicImage
from .cocoannotation import CocoAnnotation
from .cococategory import CocoCategory
from .cocodataformat import CocoDataFormat
from .cocoimage import CocoImage

IMAGES_PATH = pathlib.Path("images")
ANNOTATIONS_PATH = pathlib.Path("annotations")


def create_coco_directory_structure(path: pathlib.Path):
    """Creates the coco directory structure.

    The structure has to following form:
    path
        -images
        -annotations

    Args:
        path: Path where the coco dataset is created.
    """
    path.mkdir(parents=True, exist_ok=True)
    (path / IMAGES_PATH).mkdir(exist_ok=True)
    (path / ANNOTATIONS_PATH).mkdir(exist_ok=True)


def draw_image_to_disk(sodic_image: SodicImage, export_path: pathlib.Path):
    """Draws the image and stores it to disk.

    Args:
        sodic_image: Sodic image to draw.
        export_path: Export path of the drawn image.
    """
    drawed_image = sodic_image.draw()
    drawed_image.save(export_path)


def create_coco_dataset(
    sodic_images: List[SodicImage], category_list: List[str], export_path: pathlib.Path
) -> None:
    """Creates a coco dataset based on given sodic images."""
    create_coco_directory_structure(export_path)

    coco_images = list()
    coco_annotations = list()
    for image_id, sodic_image in enumerate(sodic_images):
        file_name = f"image{image_id}.png"
        draw_image_to_disk(sodic_image, export_path / IMAGES_PATH / file_name)

        coco_image = CocoImage.FromSodicImage(
            sodic_image, file_name=file_name, id=image_id
        )
        coco_images.append(coco_image)

        for annotation_id, drawable in enumerate(sodic_image.iter_drawables()):
            coco_annotation = CocoAnnotation.FromDrawable(
                drawable, category_list, image_id, annotation_id
            )
            coco_annotations.append(coco_annotation)

    coco_categories = list()
    for category_id, category in enumerate(category_list):
        coco_category = CocoCategory(category_id, category)
        coco_categories.append(coco_category)

    coco_data_format = CocoDataFormat(
        images=coco_images, annotations=coco_annotations, categories=coco_categories
    )
    coco_data_format_json = coco_data_format.to_json()
    with open(export_path / "instances_train.json", "w") as f:
        json.dump(coco_data_format_json, f, indent=4)
