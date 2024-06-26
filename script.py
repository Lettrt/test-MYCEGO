import os
from PIL import Image, UnidentifiedImageError
from typing import List


def load_images(folder_list: List[str], base_path:str) -> List[Image.Image]:
    """
    Функция для загрузки изображений для дальнейшей обработки
    :param folder_list: Массив с именами директорий, в которых храняться изображения
    :param base_path: Путь к базовой директории, в которой храняться директории с изображениями
    :return: Список объектов Image.Image - загруженные из дирректорий изображения
    """
    images = []
    for folder in folder_list:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            print(f'Директория не найдена: {folder_path}')
            continue
        try:
            filenames = [f for f in os.listdir(folder_path) if f.endswith(('.png',))]
        except OSError as e:
            print(f'Ошибка доступа к директории {folder_path}: {e}')
            continue
        for filename in filenames:
            image_path = os.path.join(folder_path, filename)
            try:
                image = Image.open(image_path)
                images.append(image)
            except (UnidentifiedImageError, OSError) as e:
                print(f'Ошибка загрузки изображения {image_path}: {e}')
    return images


def create_new_image(images: List[Image.Image], output_name: str) -> None:
    """
    Функция обрабатывает массив изображений и сохраняет в один tif файл
    :param images: Список изображений
    :param output_name: Имя выходного файла, в который сохраняется результат
    :return: функция ничего не возвращает
    """
    if images:
        try:
            images[0].save(output_name, save_all=True, append_images=images[1:], format='TIFF')
            print(f'Изображение успешно сохранено')
        except OSError as e:
            print(f'Ошибка сохранения нового изображения {output_name}: {e}')
    else:
        print('Нет сохраненных изображений')
