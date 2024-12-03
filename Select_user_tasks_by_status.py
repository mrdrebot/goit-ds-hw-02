import sqlite3

def execute_query(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT *
FROM tasks
WHERE user_id LIKE "2";
"""

print(execute_query(sql_script))

