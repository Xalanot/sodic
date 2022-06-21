import pytest

from sodic.image import SodicImage


@pytest.mark.parametrize("width,height", [(100, 100), (200, 100), (50, 300)])
def test_image_has_correct_width_and_height(width: int, height: int) -> None:
    sodicImage = SodicImage(width, height, [])

    image = sodicImage.draw()

    assert image.size == (width, height)
