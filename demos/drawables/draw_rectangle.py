from sodic.drawables import Rectangle

from PIL import Image, ImageDraw


def draw_simple_rectangle():
    rectangle = Rectangle(10, 10, 60, 60, "red")

    image = Image.new("RGB", (100, 100), color=(255, 255, 255))
    image_draw = ImageDraw.Draw(image)

    rectangle.draw(image_draw)

    image.save("simple_rectangle.png")


if __name__ == "__main__":
    draw_simple_rectangle()
