from PIL import Image, ImageDraw

from sodic.drawables import Triangle


def draw_simple_triangle():
    triangle = Triangle(10, 10, 10, 60, 60, 60, "red")

    image = Image.new("RGB", (100, 100), color=(255, 255, 255))
    image_draw = ImageDraw.Draw(image)

    triangle.draw(image_draw)

    image.save("simple_triangle.png")


def draw_segmentation_outline():
    triangle = Triangle(10, 10, 10, 60, 60, 60, "red")
    segmentation = triangle.segmentation

    image = Image.new("RGB", (100, 100), color="white")
    image_draw = ImageDraw.Draw(image)

    triangle.draw(image_draw)
    image_draw.polygon(segmentation.outline, outline="blue", fill=None)

    image.save("plots/segmentation_outline_triangle.png")


def draw_bounding_box():
    triangle = Triangle(10, 10, 10, 60, 60, 60, "red")
    bbox = triangle.bbox

    image = Image.new("RGB", (100, 100), color="white")
    image_draw = ImageDraw.Draw(image)

    triangle.draw(image_draw)
    image_draw.rectangle(
        [bbox.x, bbox.y, bbox.x + bbox.width, bbox.y + bbox.height],
        outline="blue",
        fill=None,
    )

    image.save("plots/bounding_box_triangle.png")


if __name__ == "__main__":
    draw_simple_triangle()
    draw_segmentation_outline()
    draw_bounding_box()
