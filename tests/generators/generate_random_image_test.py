import numpy as np

from sodic.drawables import Circle, Rectangle
from sodic.generators.generaterandomimage import generate_random_images
from sodic.generators.specifications import (
    ImageBoundingBoxGenerationSpecification,
    ImageDrawbaleGenerationSpecification,
)
from sodic.image import SodicImage


def test_random_image_generation():
    np.random.seed(1)
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

    expected_images = [
        SodicImage(
            width=image_shape[0],
            height=image_shape[1],
            drawables=[
                Circle(
                    x=67.95890265047358,
                    y=42.123043253152574,
                    radius=29.730673315367536,
                    color="orange",
                ),
                Rectangle(
                    x1=3.093966286330336,
                    y1=13.528997966984251,
                    x2=22.87277927112867,
                    y2=32.86719178602162,
                    color="red",
                ),
            ],
        ),
        SodicImage(
            width=image_shape[0],
            height=image_shape[1],
            drawables=[
                Rectangle(
                    x1=48.99582581611909,
                    y1=21.899869333250415,
                    x2=96.84605929928395,
                    y2=79.82467192170337,
                    color="red",
                ),
                Circle(
                    x=14.554125337171985,
                    y=64.22085070521389,
                    radius=13.22739854641499,
                    color="blue",
                ),
                Rectangle(
                    x1=23.026923335790453,
                    y1=10.22253204938087,
                    x2=42.00990919932343,
                    y2=30.604949137817666,
                    color="green",
                ),
            ],
        ),
        SodicImage(
            width=image_shape[0],
            height=image_shape[1],
            drawables=[
                Rectangle(
                    x1=23.18050616233358,
                    y1=21.947507471459044,
                    x2=82.51428832949179,
                    y2=82.16496459142152,
                    color="green",
                ),
                Rectangle(
                    x1=2.3509436477135686,
                    y1=69.96703243605684,
                    x2=22.46381262082926,
                    y2=89.74042834433735,
                    color="red",
                ),
            ],
        ),
    ]
    assert images == expected_images
