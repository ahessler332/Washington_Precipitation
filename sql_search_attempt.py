#takes user input to pull selected data from database
#starts off with userinput0 finding what database to work in
#userinput 1 leaves pogram open for user to work within database
#functions in a while loop, looping within the same database


import sqlite3, csv
from pathlib import Path
def main():
    
    userinput0 = input("enter the name of the database to open (include .db or file is created instead): ")
    con = sqlite3.connect(str(userinput0))
    cur = con.cursor()
    answer = " "
    while answer != "quit":
        userinput1 = " "
        userinput1 = input("enter the search function to pull selected data from the database. E.g. (SELECT column FROM table): ")
        

        try:
            if "." in userinput1:
                cur.execute(str(userinput1))
                print(cur.fetchall())
                answer = input("to exit program, type 'quit', otherwise, click enter: ")
            else:

                cur.execute(str(userinput1) + ";")
                print(cur.fetchall())
                answer = input("to exit program, type 'quit', otherwise, click enter: ")
        except:
            print("something was wrong with the given statement")
            quit

if __name__ == "__main__":
    main()







