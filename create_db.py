import sqlite3

def create_db():
# читаємо файл зі скриптом для створення БД
    with open('database_config.sql', 'r') as sql_scripts:
        create_base_tables = sql_scripts.read()

# створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect('database_config.db') as base_connect:
        cur = base_connect.cursor()
# виконуємо скрипт із файлу, який створить таблиці в БД
        # print(create_base_tables)
        cur.executescript(create_base_tables)

if __name__ == "__main__":
    create_db()
