import os
from script import (
    load_images, create_new_image
)

folder_names = ['1369_12_Наклейки', '1388_2_Наклейки 3-D_1']
BASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'tests_images')


def main():
    images = load_images(folder_names, BASE_PATH)
    create_new_image(images, 'result.tif')


if __name__ == '__main__':
    main()
