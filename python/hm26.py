"""
Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
Отдельно список папок/Отдельно список файлов
Пример запуска
python script.py /home/user/documents
Пример вывода
Содержимое директории '/home/user/documents':
Папки:
- folder1
- folder2
Файлы:
- file1.txt
- file2.txt
- notes.docx
"""

import sys, os

if len(sys.argv) < 2:
    print("Введите аргументы в таком формате: hm26.py /ПУТЬ")
    sys.exit(1)

if not os.path.isdir(sys.argv[1]):
    print("Указанный путь не является директорией")
    sys.exit(1)

file = []
dir = []

for i in os.listdir(sys.argv[1]):
    if os.path.isfile(i):
        file.append(i)
    else:
        dir.append(i)

print("\nПапки:")
for i in dir:
    print(f"-{i}")

print("\nФайлы:")
for j in file:
    print(f"-{j}")

"""
Напишите программу, которая:
Принимает путь к директории и расширение файлов через аргумент командной строки.
Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
Спрашивает у пользователя, хочет ли он удалить найденные файлы.
Если пользователь подтверждает, удаляет их.

Пример запуска: python script.py /home/user/PycharmProjects/project1 .log

Пример вывода
Найдены файлы с расширением '.log':
- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log

Вы хотите удалить эти файлы? (y/n): y
Удаление завершено.
"""

if len(sys.argv) < 3:
    print("Введите аргументы в таком формате: hm26.py /ПУТЬ .РАСШИРЕНИЕ")
    sys.exit(1)

if not os.path.isdir(sys.argv[1]):
    print("Указанный путь не является директорией")
    sys.exit(1)

dir = sys.argv[1]
ext = sys.argv[2]
res = []

for a, b, c in os.walk(dir):
    for file in c:
        if file.endswith(ext):
            res.append(os.path.join(a, file))

if res:
    print(f"\nНайдены файлы с расширением '{ext}':")
    for f in res:
        print(f"- {os.path.relpath(f, dir)}")
else:
    print(f"Файлы с расширением '{ext}' не найдены.")
    sys.exit(0)

# Подтверждение удаления
confirm = input("\nВы хотите удалить эти файлы? (y/n): ").strip()
if confirm == 'y':
    for f in res:
        try:
            os.remove(f)
        except Exception as e:
            print(f"Ошибка при удалении {f}: {e}")
    print("Удаление завершено.")
else:
    print("Удаление отменено.")




