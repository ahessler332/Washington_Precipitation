import sqlite3, csv


con = sqlite3.connect("sqlite3database.db")
cur = con.cursor()
cur.execute("DROP TABLE hydrology")
cur.execute("CREATE TABLE hydrology (site TEXT, date TEXT,  precip INTEGER, condition TEXT);")
testfile =(r"C:\Users\alexh\Documents\Geology\Python_Geology\Hydrology_Fall_City.csv")
#rows = csv.reader(a_file)
record = []
with open(testfile,'r') as file:
            next(file)
            for line in file:
                line = line.strip('\n')
                record.append(line)
                
print(record)
print(type(record))
cur.executemany("INSERT INTO hydrology VALUES (?, ?, ?, ?)", record,)

cur.execute("SELECT * FROM hydrology")
print(cur.fetchall())

con.commit()
con.close()
