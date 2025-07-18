"""
Реализуйте программу, которая должна: Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.

Пример вывода:
15/03/2025
01.12.2024
09-09-2023
28/02/2022
"""

import re

text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."
pattern = r'\b\d{2}([./-])\d{2}\1\d{4}\b'
dates = re.findall(pattern, text)
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group())

"""
Реализуйте программу, которая должна:
Прочитать строку с тегами, введёнными пользователем.
Разделить её на отдельные теги, независимо от того, чем они были разделены (запятые, точки с запятой, слэши или пробелы).
Удалить лишние пробелы и пустые значения.

Пример вывода:
['python', 'data-scince', 'machine-learning', 'AI', 'neural-networks']
"""

tag_input = "python, data-scienze / machine-learning; AI neural-networks"
raw_tags = re.split(r"[,\;/\s]+", tag_input)
cleaned_tags = [tag.strip() for tag in raw_tags if tag.strip()]

print(cleaned_tags)











































