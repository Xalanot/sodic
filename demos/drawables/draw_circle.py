from PIL import Image, ImageDraw

from sodic.drawables import Circle


def draw_simple_circle():
    circle = Circle(50, 50, 50, "red")

    image = Image.new("RGB", (100, 100), color="white")
    image_draw = ImageDraw.Draw(image)

    circle.draw(image_draw)

    image.save("plots/simple_circle.png")


def draw_segmentation_outline():
    circle = Circle(50, 50, 20)
    segmentation = circle.segmentation

    image = Image.new("RGB", (100, 100), color="white")
    image_draw = ImageDraw.Draw(image)

    circle.draw(image_draw)
    image_draw.polygon(segmentation.outline, outline="blue", fill=None)

    image.save("plots/segmentation_outline_rectangle.png")


def draw_bounding_box():
    circle = Circle(50, 50, 20)
    bbox = circle.bbox

    image = Image.new("RGB", (100, 100), color="white")
    image_draw = ImageDraw.Draw(image)

    circle.draw(image_draw)
    image_draw.rectangle(
        [bbox.x, bbox.y, bbox.x + bbox.width, bbox.y + bbox.height],
        outline="blue",
        fill=None,
    )

    image.save("plots/bounding_box_circle.png")


if __name__ == "__main__":
    draw_simple_circle()
    draw_segmentation_outline()
    draw_bounding_box()
