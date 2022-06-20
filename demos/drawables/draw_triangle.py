from sodic.drawables import Triangle

from PIL import Image, ImageDraw


def draw_simple_triangle():
    triangle = Triangle(10, 10, 10, 60, 60, 60, "red")

    image = Image.new("RGB", (100, 100), color=(255, 255, 255))
    image_draw = ImageDraw.Draw(image)

    triangle.draw(image_draw)

    image.save("simple_triangle.png")


if __name__ == "__main__":
    draw_simple_triangle()
