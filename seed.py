import faker
from random import randint, choice
import sqlite3
from create_db import create_db

NUMBER_USERS = 3
NUMBER_TASKS = 10
STATUS_TYPES = [('new',), ('in progress',), ('completed',)] # status type list

def generate_fake_data(number_users, number_tasks) -> tuple():
    fake_users_names = []
    fake_users_emails = []
    fake_tasks_titles = []
    fake_tasks_descriptions = []

    fake_data = faker.Faker()

# Generate users
    for _ in range(number_users):
        fake_users_names.append(fake_data.name())

# Generate users emails
    for _ in range(number_users):
        fake_users_emails.append(fake_data.email())

# Generate tasks titles
    for _ in range(number_tasks):
        fake_tasks_titles.append(fake_data.catch_phrase())

# Generate task descriptions
    for _ in range(number_tasks):
        fake_tasks_descriptions.append(fake_data.text(max_nb_chars=100))

    return fake_users_names, fake_users_emails, fake_tasks_titles, fake_tasks_descriptions

def prepare_data(users_name, emails, tasks_titles, tasks_descriptions) -> tuple():
    # Create a list of user tuples
    for_users = []
    for name in users_name:
        email = choice(emails)
        for_users.append((name, email))
        emails.remove(email)

    # Create a list of task tuples
    for_tasks = []
    for task in tasks_titles:
        for_tasks.append((task, choice(tasks_descriptions), randint(1, len(STATUS_TYPES)), randint(1, NUMBER_USERS)))

    return for_users, for_tasks

def insert_data_to_db(users, status, tasks) -> None:
    # Create connection with our DB and will get cursor object for data manipulation
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        # Create script to add users data in the DB      
        sql_to_users = """INSERT INTO users(fullname, email)
                               VALUES (?, ?)"""
        # Add users data in the DB
        cur.executemany(sql_to_users, users)

        # Create script to add status types in the DB
        sql_to_statuses = """INSERT INTO status(name)
                               VALUES (?)"""
        # Add status types in the DB
        cur.executemany(sql_to_statuses, status)

        # Create script to add tasks in the DB
        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                              VALUES (?, ?, ?, ?)"""
        # Add tasks in the DB
        cur.executemany(sql_to_tasks, tasks)

        # Fix changes in the DB
        con.commit()

if __name__ == "__main__":
    create_db() # create DB and drop tabels
    user_table, task_table = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_TASKS))
    insert_data_to_db(user_table, STATUS_TYPES, task_table)