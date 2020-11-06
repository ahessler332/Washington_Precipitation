
import sqlite3, csv
import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt 


userinput0 = input("enter the name of the database to open (include .db or file is created instead): ")
userinput1 = input("enter 'weekly' for a weekly graph, 'monthly' for a monthly graph, and 'yearly' for a yearly graph.")
if userinput1 == "weekly":
    time = 6
elif userinput1 == 'monthly':
    time = 29
elif userinput1 == 'yearly':
    time = 364
else:
    print("input not valid")
userinput2 = input("enter name of the column that holds the time values: ")
userinput3 = input("enter name of the column that is being measured: ")
userinput4 = input("enter name of the table that is being used within the database: ")
database = userinput0
con = sqlite3.connect(database)
cur = con.cursor()

def timebreakdown (userinput1):
    cur.execute("SELECT "+str(userinput2) +", " +str(userinput3)+" FROM " + str(userinput4) + ";")
    data = cur.fetchall()
    dates = []
    precipitation = []
    precipcounter = 0
    datecounter = 0
    precip = 0

    for row in data:
        if precipcounter < time:
            precip = precip + row[1]
            precipcounter = precipcounter + 1 
        else:
            precipitation.append(precip)
            precipcounter = 0
            precip = 0
    for row in data:
        if datecounter < time:
            datecounter = datecounter + 1 
        else:
            dates.append(row[0])
            datecounter = 0
#combine counters and for loops into one
    return dates, precipitation        




def plot_data(dates, precipitation):
    cur.execute("SELECT "+str(userinput2)+","+str(userinput3)+" FROM " + str(userinput4) + ";")        

    
    plt.bar(dates,precipitation, color = 'blue', width = 0.4)##line style
    plt.show()
    


if __name__ == "__main__":
    dates, precipitation = timebreakdown(userinput1)
    plot_data(dates, precipitation)
    con.close()    

