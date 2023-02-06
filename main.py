import os


directory = '/Users/derendyaevka/Desktop/rename_files/txt_files'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # Функция isfile() модуля os.path возвращает True если путь path существует и является обычным файлом
    if os.path.isfile(f) and filename != '.DS_Store':
        with open(f) as file:
            field_name = file.readline()
            needed_name = os.path.join(directory, f'{field_name} - {filename}')
            os.rename(f, needed_name)
