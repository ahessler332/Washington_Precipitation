"""
This script will handle the main interactions with the user
as they query the database


code from: https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
https://www.sqlitetutorial.net/sqlite-python/

One of the issues is we need to rename the headings of the csv files so that there simple and short
"""
import sqlite3


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Catalog")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Catalog WHERE Site_Code=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)



def main():
    database = r'sqlite.db'

    # create a database connection
    conn = conn = sqlite3.connect(r'sqlite.db')

    with conn:
        print("1. Query task by priority:")
        select_task_by_priority(conn, '27u')


        #prints out name of column names
        cursor = conn.execute('select * from Catalog')
        names = list(map(lambda x: x[0], cursor.description))
        print(names)


       # print("2. Query all tasks")
       # select_all_tasks(conn)


if __name__ == '__main__':
    main()