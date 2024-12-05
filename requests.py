import sqlite3

# Get all tasks by user id
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

# print(select_user_tasks_by_user(sql_script))

# Select_user_tasks_by_status
def select_user_tasks_by_status(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT *
FROM tasks
WHERE status_id = (
    SELECT id FROM status WHERE name = 'new'
);
"""

# print(select_user_tasks_by_status(sql_script))

# Update the status of a specific task
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

# Select users who have not tasks
def select_users_no_tasks(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT *
FROM users
WHERE id NOT IN (
    SELECT DISTINCT user_id
    FROM tasks
    WHERE user_id IS NOT NULL
);
"""
# print(select_users_no_tasks(sql_script))

# Insert special task to special user
def insert_task_to_user(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('New Task', 'Description of the new task', 1, 2);
"""
# print(insert_task_to_user(sql_script))
# print(select_user_tasks_by_user(sql_script))

# Get all tasks that are not yet finished
def select_not_finished_tasks(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT *
FROM tasks
WHERE status_id IN (
    SELECT id FROM status WHERE name != 'completed'
);
"""
# print(select_not_finished_tasks(sql_script))

# Delete task by id
def delete_tasks_by_id(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
DELETE FROM tasks WHERE id = 13;
"""
# print(delete_tasks_by_id(sql_script))

# Select user by email
def select_user_by_email(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT *
FROM users
WHERE email LIKE "christinemiles@example.net";
# """
# print(select_user_by_email(sql_script))

# Update user name
def update_user_name(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
UPDATE users
SET fullname = "Jonh Dou"
WHERE id = 2;
"""
# print(select_user_by_email(sql_script))

# Count tasks by status
def count_tasks_by_status(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT s.name AS status_name, COUNT(t.id) AS task_count
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.id, s.name;
"""
# print(count_tasks_by_status(sql_script))

# Count tasks by status
def count_tasks_by_status(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT s.name AS status_name, COUNT(t.id) AS task_count
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.id, s.name;
"""
# print(count_tasks_by_status(sql_script))

# Select tasks by email domen
def select_tasks_by_email_domen(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT t.id AS task_id, t.title, t.description, u.fullname, u.email, s.name AS status_name
FROM tasks t
JOIN users u ON t.user_id = u.id
JOIN status s ON t.status_id = s.id
WHERE u.email LIKE '%@example.org';

"""
# print(select_tasks_by_email_domen(sql_script))

# Select tasks which have not description
def select_tasks_by_non_description(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT *
FROM tasks
WHERE description = '';
"""
# print(select_tasks_by_non_description(sql_script))

# Select users and tasks by status
def select_users_and_tasks_by_status(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT u.id AS user_id, u.fullname, u.email, t.id AS task_id, t.title, t.description, s.name AS status_name
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';
"""
# print(select_tasks_by_non_description(sql_script))

# Select users and count they tasks
def select_users_and_count_tasks(sql_script: str) -> list:
    with sqlite3.connect('database.db') as base_connect:
        cur = base_connect.cursor()
        cur.execute(sql_script)
        return cur.fetchall()

sql_script = """
SELECT u.id AS user_id, u.fullname, u.email, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.id, u.fullname, u.email;

"""
# print(select_users_and_count_tasks(sql_script))