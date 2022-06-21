from PIL import Image, ImageDraw

from sodic.drawables import Circle


def draw_simple_circle():
    circle = Circle(50, 50, 50, "red")

    image = Image.new("RGB", (100, 100), color=(255, 255, 255))
    image_draw = ImageDraw.Draw(image)

    circle.draw(image_draw)

    image.save("simple_circle.png")


if __name__ == "__main__":
    draw_simple_circle()
