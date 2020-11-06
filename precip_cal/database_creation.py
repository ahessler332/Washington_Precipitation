import sqlite3, csv
from pathlib import Path

#requires 6 inputs from the user for required data. seventh input from user is to continue program for another round
#or quit pogram.
#user input 0 takes in what database to work in, user input 1 takes name of new table
#user input 2 takes the column names and data type, while userinput 3 just takes name of the columns without the data type
#(this is necessary for INSERT method and to avoid slicing strings)
#userinput 4 takes in the number of columns to be created, which is then filtered to create the number of placeholders to be made
#(this is seen with all the elif statements, with current capacity between 1 placeholder up to 8 placeholder values)
#userinput 5 takes in file path and converts it using pathlib to be usable for python (convenient when sqlite tools required manual changing of file path to function)
#Inserts each line of a csv file rather than build one big list for insertion
#repeats program in working in same database in while loop. If wanting to change database, must exit script and restart
def main ():

    userinput0 = input("Enter name of database to either be created or open (please include .db in name): ")
    try:
        con = sqlite3.connect(str(userinput0))
        cur = con.cursor()
    except:
        print("something was wrong with the database name.")
        quit    
    answer = " "
    while answer != "quit pogram":
        userinput1 = input("please enter name of sql table to be created: ")
        userinput2 = input("please enter the columns and data types for the sql table: ")
        userinput3 = input("please enter name of the columns without the data types: ")
        userinput4 = input("how many columns will be created? please enter numerical response: ")

        try:
            cur.execute("DROP TABLE IF EXISTS " + str(userinput1))
            cur.execute("CREATE TABLE " + str(userinput1) + " (" + str(userinput2) + ")")
        except :
            print("something was wrong with the information given. unable to create table.")
            quit

        try:
            userinput5 = input("Enter full file path for file to be imported to data table: ")
            filepath = Path(str(userinput5))
            userfile =(filepath)
        except:
            print("something was wrong with the file path given.")
            quit


        if userinput4 == "0":
            quit
            print("Program needs columns to create the database.")
        elif userinput4 == "1":
            values = "(?)"
        elif userinput4 == "2":
            values = "(?, ?)"
        elif userinput4 == "3":
            values = "(?, ?, ?)"
        elif userinput4 == "4":
            values = "(?, ?, ?, ?)"
        elif userinput4 == "5":
            values = "(?, ?, ?, ?, ?)"
        elif userinput4 == "6":
            values = "(?, ?, ?, ?, ?, ?)"
        elif userinput4 == "7":
            values = "(?, ?, ?, ?, ?, ?, ?)"
        elif userinput4 == "8":
            values = "(?, ?, ?, ?, ?, ?, ?, ?)"
        else:
            print("You've entered a number too large or 0 of columns to be created")


        with open(userfile,'r') as file:

            next(file)
            for line in file:
                line = line.strip('\n')
                line = line.split(",")
                cur.execute("INSERT INTO "+ str(userinput1) +" (" + str(userinput3) +") VALUES " + values, line)
                

        print("Successfully uploaded csv file into database.")
        #cur.execute("SELECT * FROM " + str(userinput1) +";")
        #print(cur.fetchall())
        answer = input("If you would like to exit the program, type 'quit pogram': ")
        

    con.commit()
    con.close()

if __name__ == '__main__':
    main()
#end of program    
