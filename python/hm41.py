"""
Используя базу данных world, выведи названия всех стран из таблицы country. Каждое название должно отображаться с новой
строки и иметь номер.

Пример вывода:
1. Aruba
2. Afghanistan
3. Angola
...
239. Zimbabwe
"""

import pymysql

connection = pymysql.connect(
    host='ich-db.edu.itcareerhub.de',
    user='ich1',
    password='password',
    database='world',
    cursorclass=pymysql.cursors.Cursor
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT Name FROM country ORDER BY Name")
        countries = cursor.fetchall()

        for i, (name,) in enumerate(countries, start=1):
            print(f"{i}. {name}")

finally:
    connection.close()

"""
Добавьте к предыдущей программе возможность выбора страны. Пользователь введёт название или номер из выведенного списка.
Далее выведите все города этой страны и их численность населения, также с нумерацией.

Введите страну: Germany  
Berlin — 3386667
Hamburg — 1704735
Munich [München] — 1194560
...
"""

connection = pymysql.connect(
    host='ich-db.edu.itcareerhub.de',
    user='ich1',
    password='password',
    database='world',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT Code, Name FROM country ORDER BY Name")
        countries = cursor.fetchall()

        country_list = []
        for i, country in enumerate(countries, start=1):
            print(f"{i}. {country['Name']}")
            country_list.append(country)

        user_input = input("\nВведите страну (название или номер): ").strip()

        selected_country = None
        if user_input.isdigit():
            index = int(user_input) - 1
            if 0 <= index < len(country_list):
                selected_country = country_list[index]
        else:
            for c in country_list:
                if c["Name"].lower() == user_input.lower():
                    selected_country = c
                    break

        if not selected_country:
            print("Страна не найдена.")
        else:
            code = selected_country["Code"]
            print(f"\nГорода страны {selected_country['Name']}:\n")

            cursor.execute("""
                SELECT Name, Population FROM city 
                WHERE CountryCode = %s 
                ORDER BY Population DESC
            """, (code,))
            cities = cursor.fetchall()

            for i, city in enumerate(cities, start=1):
                print(f"{i}. {city['Name']} — {city['Population']}")

finally:
    connection.close()
