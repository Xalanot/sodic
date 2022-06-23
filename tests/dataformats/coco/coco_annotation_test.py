from sodic.dataformats.coco import CocoAnnotation
from sodic.drawables import Rectangle


def test_coco_annotation_converts_to_correct_json():
    segmentation = [[10, 10, 60, 10, 60, 60, 10, 60]]
    area = 2500
    bbox = [10, 10, 50, 50]
    image_id = 1
    id = 1
    category_id = 0
    coco_annotation = CocoAnnotation(
        segmentation=segmentation,
        area=area,
        bbox=bbox,
        image_id=image_id,
        id=id,
        category_id=category_id,
    )

    coco_annotation_json = coco_annotation.to_json()

    expected_coco_annotation_json = {
        "segmentation": segmentation,
        "area": area,
        "bbox": bbox,
        "image_id": image_id,
        "id": id,
        "category_id": category_id,
    }
    assert coco_annotation_json == expected_coco_annotation_json


def test_create_coco_annotation_from_drawable():
    rectanlge = Rectangle(10, 10, 60, 60)
    category_list = ["rectangle"]
    image_id = 1
    id = 1
    category_id = 0
    segmentation = [[10, 10, 60, 10, 60, 60, 10, 60]]
    area = 2500
    bbox = [10, 10, 50, 50]

    coco_annotation = CocoAnnotation.FromDrawable(
        drawable=rectanlge, category_list=category_list, image_id=image_id, id=id
    )

    expected_coco_annotation = CocoAnnotation(
        segmentation=segmentation,
        area=area,
        bbox=bbox,
        image_id=image_id,
        id=id,
        category_id=category_id,
    )
    assert coco_annotation == expected_coco_annotation
