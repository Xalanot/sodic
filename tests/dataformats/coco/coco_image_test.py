from sodic.dataformats.coco import CocoImage
from sodic.image import SodicImage


def test_coco_image_converts_to_correct_json():
    width = 100
    height = 100
    file_name = "image.png"
    id = 1
    coco_image = CocoImage(file_name=file_name, height=height, width=width, id=id)

    coco_image_json = coco_image.to_json()

    expected_coco_image_json = {
        "file_name": file_name,
        "height": height,
        "width": width,
        "id": id,
        "license": 0,
    }
    assert coco_image_json == expected_coco_image_json


def test_create_coco_image_from_sodic_image():
    width = 100
    height = 100
    file_name = "image.png"
    id = 1
    sodic_image = SodicImage(width=width, height=height, drawables=[])

    coco_image = CocoImage.FromSodicImage(
        sodic_image=sodic_image, file_name=file_name, id=id
    )

    expected_coco_image = CocoImage(
        file_name=file_name, height=height, width=width, id=id
    )
    assert coco_image == expected_coco_image
