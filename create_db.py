import sqlite3

def create_db():
    # Read script file to create DB
    with open('database_config.sql', 'r') as sql_scripts:
        create_base_tables = sql_scripts.read()

    # Create connection with DB 
    with sqlite3.connect('database.db') as base_connect:
        base_connect.execute("PRAGMA foreign_keys = ON;")
        cur = base_connect.cursor()
        # Create tables in th DB fron script file
        cur.executescript(create_base_tables)

if __name__ == "__main__":
    create_db()
