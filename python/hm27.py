"""
Напишите программу, которая ищет в файле все строки, содержащие указанное пользователем слово, и сохраняет их в новый
файл.
Имя нового файла формируется как <keyword>_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Если совпадения не найдены, новый файл не создаётся.

Используйте файл system_log.txt.
Пример ввода:
Введите имя файла для поиска: system_log.txt
Введите ключевое слово: error

Пример вывода:
Строки, содержащие 'error', сохранены в error_system_log.txt.
"""

import os

src_name = input("Введите имя файла для поиска: ")
key = input("Введите ключевое слово: ")

if not os.path.isfile(src_name):
    print("Ошибка: файл не найден.")
else:
    with open(src_name, 'r', encoding='utf-8') as src:
        lines = src.readlines()

    match_lines = list(filter(lambda ln: key.lower() in ln.lower(), lines))

    if match_lines:
        out_name = f"{key}_{src_name}"
        with open(out_name, 'w', encoding='utf-8') as out:
            out.writelines(match_lines)
        print(f"Строки, содержащие '{key}', сохранены в {out_name}.")
    else:
        print(f"Совпадений с '{key}' не найдено. Файл не создан.")

"""
Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
Имя нового файла формируется как unique_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Исходный порядок строк должен сохраниться.
Если в файле нет дубликатов, создаётся точная копия файла.

Используйте файл movies_to_watch.txt.

Пример ввода:
Введите имя файла: movies_to_watch.txt
Пример вывода:
Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.
"""

import os

filename = input("Введите имя файла: ")

if not os.path.isfile(filename):
    print("Ошибка: файла не существует или название введено некорректно.")
else:
    with open(filename, 'r', encoding='utf-8') as r_file:
        lines = r_file.readlines()

    seen = set()
    unique_lines = []

    for line in lines:
        if line not in seen:
            unique_lines.append(line)
            seen.add(line)

    new_filename = f"unique_{filename}"

    with open(new_filename, 'w', encoding='utf-8') as w_file:
        w_file.writelines(unique_lines)

    print(f"Дубликаты удалены. Уникальные строки сохранены в {new_filename}.")
