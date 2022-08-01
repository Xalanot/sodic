from matplotlib import pyplot as plt

from sodic.generators.generaterandomimage import generate_random_images
from sodic.generators.specifications import (
    ImageBoundingBoxGenerationSpecification,
    ImageDrawbaleGenerationSpecification,
)


def draw_random_images():
    drawable_specs = [
        ImageDrawbaleGenerationSpecification("rectangle", ["red", "green"], 1),
        ImageDrawbaleGenerationSpecification("circle", ["blue", "orange"], 0.5),
    ]
    bbox_specs = [
        ImageBoundingBoxGenerationSpecification([(60, 60), (20, 20)], (0.01, 0.02), 2),
        ImageBoundingBoxGenerationSpecification(
            [(30, 30), (20, 20), (50, 55)], (0.05, 0.03), 1
        ),
    ]
    image_shape = (100, 100)
    images_to_draw = 3

    images = generate_random_images(
        image_shape, drawable_specs, bbox_specs, images_to_draw
    )

    for image in images:
        plt.imshow(image.draw())
        plt.show()


if __name__ == "__main__":
    draw_random_images()
