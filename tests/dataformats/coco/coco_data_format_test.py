from sodic.dataformats.coco import (
    CocoAnnotation,
    CocoCategory,
    CocoDataFormat,
    CocoImage,
)


def test_coco_data_format_converts_to_correct_json():
    image_json = {
        "file_name": "image.png",
        "height": 100,
        "width": 100,
        "id": 0,
        "license": 0,
    }
    annotation_json = {
        "segmentation": [[10, 10, 60, 10, 60, 60, 10, 60]],
        "area": 2500,
        "bbox": [10, 10, 50, 50],
        "image_id": 0,
        "id": 0,
        "category_id": 0,
    }
    category_json = {"id": 0, "name": "rectangle", "supercategory": "geometry"}
    info_json = {
        "year": 2022,
        "version": "",
        "description": "",
        "contributor": "",
        "url": "",
        "date_created": "",
    }
    license_json = {"id": 0, "name": "", "url": ""}
    coco_data_format = CocoDataFormat(
        images=[
            CocoImage(
                file_name=image_json["file_name"],
                height=image_json["height"],
                width=image_json["width"],
                id=image_json["id"],
            )
        ],
        annotations=[
            CocoAnnotation(
                segmentation=annotation_json["segmentation"],
                area=annotation_json["area"],
                bbox=annotation_json["bbox"],
                image_id=annotation_json["image_id"],
                id=annotation_json["id"],
                category_id=annotation_json["category_id"],
            )
        ],
        categories=[CocoCategory(id=category_json["id"], name=category_json["name"])],
    )

    coco_data_format_json = coco_data_format.to_json()

    expected_coco_data_format_json = {
        "images": [image_json],
        "annotations": [annotation_json],
        "categories": [category_json],
        "info": info_json,
        "licenses": [license_json],
    }
    assert coco_data_format_json == expected_coco_data_format_json
