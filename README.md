Create a database for the task management system using SQLite.
The database should contain tables for users, task statuses, and the tasks themselves.
Execute the necessary queries in the task management system database.

Added database creation (permanent overwrite) to the seed.py file to prevent errors.

Created queries according to the task in the requests.py file. To use them:
- in DBeaver, copy sql_script without quotes and paste it into the script file;
- if you run it via the console, in the desired query, uncomment the print command and comment out all the others and run the file execution via the console