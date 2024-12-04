import sqlite3

def select_user_tasks_by_user(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT *
FROM tasks
WHERE user_id = "2";
"""

print(select_user_tasks_by_user(sql_script))

def select_user_tasks_by_status(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

# sql_script = """
# SELECT t.id, t.title, t.description, u.fullname, u.email, s.name AS status_name
# FROM tasks t
# JOIN users u ON t.user_id = u.id
# JOIN status s ON t.status_id = s.id
# WHERE t.status_id = (
#     SELECT id FROM status WHERE name = 'new'
# );
# """
sql_script = """
SELECT *
FROM tasks
WHERE status_id = (
    SELECT id FROM status WHERE name = 'new'
);
"""

# print(select_user_tasks_by_status(sql_script))

def update_tasks_status(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
UPDATE tasks
SET status_id = 3
WHERE id = 4;
"""
# print(select_user_tasks_by_status(sql_script))

def select_users_no_tasks(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT *
FROM tasks
WHERE user_id = "2";
"""
# print(select_user_tasks_by_status(sql_script))

