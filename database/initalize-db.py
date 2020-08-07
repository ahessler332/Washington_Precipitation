"""
Should only be run once or whenever we need to update database
The idea is that the database will be read-only from the users end
and this script will create a database and insert all of the information in
our csv file

Sqlite set up
https://www.sqlitetutorial.net/sqlite-python/creating-database/#:~:text=To%20create%20a%20database%2C%20first,c%3A%5Csqlite%5Cdb%20folder.


In order to access the database from terminal, your gonna want to type
'sqlite3' and then type in '.open sqlite.db'
https://www.quackit.com/sqlite/tutorial/create_a_database.cfm

(look through these quackit tutorials, they are pretty good actually)

Importing csv files into sqlite
https://www.quackit.com/sqlite/tutorial/import_data_from_csv_file.cfm

I did '.import ./Hydrology_${rest of the name}$.csv Catalog
I didn't realize this when I did this but Catalog is the name of the table
When you redo this, switch catalog to seperate names or however you want to organize the database (actually this is fine)

Other tutorial
https://www.sqlitetutorial.net/sqlite-import-csv/#:~:text=First%2C%20from%20the%20menu%20choose,shown%20in%20the%20picture%20below.


Also, when I manually imported them and in github, they said there were expected 4 columns but found 5 (but were ignored)

In the future, you may want to auotmate this process since I just did it manually through the terminal
"""


import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version) #denotes sucess
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"sqlite.db")