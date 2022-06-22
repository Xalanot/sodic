from PIL import Image, ImageDraw

from sodic.drawables import Rectangle


def draw_simple_rectangle():
    rectangle = Rectangle(10, 10, 60, 60, "red")

    image = Image.new("RGB", (100, 100), color=(255, 255, 255))
    image_draw = ImageDraw.Draw(image)

    rectangle.draw(image_draw)

    image.save("plots/simple_rectangle.png")


def draw_segmentation_outline():
    rectangle = Rectangle(10, 10, 60, 60, "red")
    segmentation = rectangle.segmentation

    image = Image.new("RGB", (100, 100), color="white")
    image_draw = ImageDraw.Draw(image)

    rectangle.draw(image_draw)
    image_draw.polygon(segmentation.outline, outline="blue", fill=None)

    image.save("plots/segmentation_outline_circle.png")


def draw_bounding_box():
    rectangle = Rectangle(10, 10, 60, 60, "red")
    bbox = rectangle.bbox

    image = Image.new("RGB", (100, 100), color="white")
    image_draw = ImageDraw.Draw(image)

    rectangle.draw(image_draw)
    image_draw.rectangle(
        [bbox.x, bbox.y, bbox.x + bbox.width, bbox.y + bbox.height],
        outline="blue",
        fill=None,
    )

    image.save("plots/bounding_box_rectangle.png")


if __name__ == "__main__":
    draw_simple_rectangle()
    draw_segmentation_outline()
    draw_bounding_box()
