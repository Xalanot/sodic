from sodic.drawables import Rectangle
from sodic.image import SodicImage


def draw_single_rectangle():
    drawables = [Rectangle(10, 10, 40, 40, "red")]
    sodicImage = SodicImage(100, 100, drawables)
    image = sodicImage.draw()
    image.save("single_rectangle.png")


if __name__ == "__main__":
    draw_single_rectangle()
