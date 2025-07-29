"""
Напишите программу, которая:
- создаёт базу данных notes_app_<your_group>_<your_full_name>
- выбирает эту базу через USE notes_app
- выводит сообщение о результате

Пример вывода:
Database 'notes_app' created or already exists.
"""

import pymysql

db_name = "notes_app_210225_ptm_daniil_boiko"

connection = pymysql.connect(
    host='ich-edit.edu.itcareerhub.de',
    user='ich1',
    password='ich1_password_ilovedbs',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute(f"USE {db_name}")
        print(f"Database '{db_name}' created or already exists and selected.")
finally:
    connection.close()

"""
Продолжите предыдущую программу:
- создайте таблицу notes с полями: id, title, content
- вставьте одну заметку в таблицу
- выполните commit() после вставки
- выведите все заметки используя DictCursor

Пример вывода: 
Note added: Shopping list
"""

db_name = "notes_app_210225_ptm_daniil_boiko"

connection = pymysql.connect(
    host='ich-edit.edu.itcareerhub.de',
    user='ich1',
    password='ich1_password_ilovedbs',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=False
)

try:
    with connection.cursor() as cursor:
        cursor.execute(f"USE `{db_name}`")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INT PRIMARY KEY AUTO_INCREMENT,
                title VARCHAR(255) NOT NULL,
                content TEXT
            )
        """)

        cursor.execute("""
            INSERT INTO notes (title, content)
            VALUES (%s, %s)
        """, ("Shopping list", "Milk, Bread, Eggs"))

        connection.commit()
        print("Note added: Shopping list")

        cursor.execute("SELECT * FROM notes")
        notes = cursor.fetchall()

        print("\nВсе заметки:")
        for note in notes:
            print(f"{note['id']}. {note['title']} — {note['content']}")

finally:
    connection.close()
