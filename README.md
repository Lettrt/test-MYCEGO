# test-MYCEGO

# Запуск проекта локально
- Склонировать проект командой git clone
- Создать виртуальное окружение
```bash
python3 -m venv venv
```
- Активировать виртуальное окружение
```bash
source /venv/bin/activate/
```
- Установить зависимости
```bash
pip3 install -r requriements.txt
```
- В файле main.py указать путь к директории с изображениями
```bash
folder_names = ['1369_12_Наклейки', '1388_2_Наклейки 3-D_1']
BASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'tests_images')
```
- Запустить программу
```bash
python3 main.py
```
- Готово!
