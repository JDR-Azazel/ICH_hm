"""
Реализовать программу, которая должна: Прочитать файл student_courses.json, содержащий:
имя, дату рождения (birth_date) в формате дд.мм.гггг, дату поступления (enrollment_date) в том же формате, список курсов.
Вычислить:
Общее количество студентов.
Средний возраст на момент поступления.
Количество студентов на каждом курсе.
Сохранить отчёт в JSON-файл student_courses_report.json.
Данные:

[
  {"name": "Diana Williams", "birth_date": "12.06.1983", "enrollment_date": "29.04.2023", "courses": ["Physics", "Chemistry"]},
  {"name": "Tina Miller", "birth_date": "06.07.2004", "enrollment_date": "18.04.2020", "courses": ["Biology", "Business"]},
  {"name": "Kevin Miller", "birth_date": "20.12.2004", "enrollment_date": "16.12.2020", "courses": ["Linguistics", "Math", "History"]},
  {"name": "Fiona Brown", "birth_date": "05.07.1999", "enrollment_date": "02.09.2022", "courses": ["Art", "Philosophy"]},
  {"name": "Charlie Davis", "birth_date": "17.07.1998", "enrollment_date": "17.05.2023", "courses": ["Chemistry", "Physics", "Business"]},
  {"name": "Diana Jones", "birth_date": "24.12.1980", "enrollment_date": "26.11.2021", "courses": ["Economics", "Linguistics"]},
  {"name": "Alice Johnson", "birth_date": "22.09.1981", "enrollment_date": "23.12.2020", "courses": ["Chemistry", "Economics", "Math"]},
  {"name": "Ian Lopez", "birth_date": "23.11.2001", "enrollment_date": "07.05.2020", "courses": ["Philosophy", "Art", "Physics"]},
  {"name": "Kevin Davis", "birth_date": "30.01.1997", "enrollment_date": "20.03.2021", "courses": ["Math", "Economics"]},
  ...
]

Пример вывода (student_courses_report.json):
{
    "total_students": 100,
    "average_enrollment_age": 27.9,
    "students_per_course": {
        "Art": 21,
        "Biology": 18,
        "Business": 28,
        "Chemistry": 16,
        "Economics": 23,
        "History": 9,
        "Linguistics": 23,
        "Math": 23,
        "Philosophy": 19,
        "Physics": 19
    }
}
"""

import json
from datetime import datetime

def compute_chrono_delta_in_years(origin_stamp, reference_stamp):
    date_proto = "%d.%m.%Y"
    born_on = datetime.strptime(origin_stamp, date_proto)
    joined_on = datetime.strptime(reference_stamp, date_proto)
    cycle_count = joined_on.year - born_on.year
    if (joined_on.month, joined_on.day) < (born_on.month, born_on.day):
        cycle_count -= 1
    return cycle_count

def initiate_student_registry_analysis():
    with open("student_courses.json", "r", encoding="utf-8") as raw_student_data:
        brain_units = json.load(raw_student_data)

    population_size = len(brain_units)
    cumulative_join_age = 0
    knowledge_stream_map = {}

    for entity in brain_units:
        age_at_enroll = compute_chrono_delta_in_years(
            entity["birth_date"], entity["enrollment_date"]
        )
        cumulative_join_age += age_at_enroll

        for discipline in entity["courses"]:
            knowledge_stream_map[discipline] = knowledge_stream_map.get(discipline, 0) + 1

    sorted_knowledge_stream_map = dict(sorted(knowledge_stream_map.items()))

    synthetic_manifest = {
        "total_students": population_size,
        "average_enrollment_age": round(cumulative_join_age / population_size, 1) if population_size else 0,
        "students_per_course": sorted_knowledge_stream_map
    }

    with open("student_courses_report.json", "w", encoding="utf-8") as dispatch_node:
        json.dump(synthetic_manifest, dispatch_node, ensure_ascii=False, indent=4)

initiate_student_registry_analysis()
