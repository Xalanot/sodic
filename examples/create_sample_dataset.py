import pathlib

from sodic.dataformats.coco.createdataset import create_coco_dataset
from sodic.drawables import Rectangle
from sodic.image import SodicImage


def main():
    first_image = SodicImage(
        width=100,
        height=100,
        drawables=[Rectangle(10, 10, 60, 60), Rectangle(70, 70, 80, 80, "blue")],
    )
    category_list = ["rectangle", "circle"]
    export_path = pathlib.Path("coco_dataset")
    create_coco_dataset([first_image], category_list, export_path)


if __name__ == "__main__":
    main()
