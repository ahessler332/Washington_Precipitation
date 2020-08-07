import Precip_month_calc as month_calc
import Precip_year_calc as year_calc
import Precip_file_list as file_list
from Precip_file_list import station
import Precip_month_breakdown as month_breakdown
import Precip_year_breakdown as year_breakdown
from prettytable import PrettyTable

file_nametuple =("Hydrology_Fall_City.csv","Hydrology_Federal_Way.csv",
                "Hydrology_Bothell.csv", "Hydrology_North_Vashon.csv",
                "Hydrology_South_Vashon.csv", "Hydrology_Mukilteo.csv",
                "Hydrology_Bellevue.csv", "Hydrology_Burien.csv",
                "Hydrology_Cougar_MT.csv", "Hydrology_Enumclaw.csv")
yearnameslist = ["1988","1989","1990","1991","1992","1993","1994",
                 "1995","1996","1997","1998","1999","2000","2001",
                 "2002","2003","2004","2005","2006","2007","2008",
                 "2009","2010","2011","2012","2013","2014","2015",
                 "2016","2017","2018","2019","2020"]
monthnameslist = ["january" , "febuary", "march", "april", "may",
             "june", "july", "august", "september", "october",
             "november", "december"]
avgyearpreciplist = []
avgdaypreciplist = []
avgmonthpreciplist = []
z = len(file_nametuple)
for q in range(z):
    
    file_list.weather_file(file_nametuple)

    month_breakdown.monthbreakdown(station)
    year_breakdown.yearbreakdown(station)

        #print("completed weather calculations")
    avgdayprecip = month_calc.weather_calc_month()[0]
        
    avgdaypreciplist.append(avgdayprecip)
    print("finished first calc")
    avgmonthprecip = month_calc.weather_calc_month()[1]
        
    avgmonthpreciplist.append(avgmonthprecip)
    print("finished second calc")
    avgyearprecip = year_calc.weather_calc_year()
        
    avgyearpreciplist.append(avgyearprecip)
        


    t = PrettyTable()
    t.field_names = ["months", "precipitation per day", "precipitation per month"]
    for k in range(12):
        t.add_row([monthnameslist[k], avgdayprecip[k], avgmonthprecip[k]]) 
    print(t)
        
    t2 = PrettyTable()
    t2.field_names = ["Years", "precipitation per year"]
    for k in range(33):
        t2.add_row([yearnameslist[k], avgyearprecip[k]])
    print(t2)
        

    avgdayprecip = []
    avgmonthprecip = []
    monthlist = []
    record = {}
    station = []
    print("finished "+file_nametuple[q])

    minlist = []
    maxlist = []
    k = 0
    q = 100000
    for y in range(len(avgyearpreciplist)):
        for t in range(len(avgyearpreciplist[y])):
            if (avgyearpreciplist[y][t]) == 0:
                pass
            elif (avgyearpreciplist[y][t]) != 0:
                k = (avgyearpreciplist[y][t])
                if float(q) > float(k):
                    q = k
                    minlist.append(q)
                else:
                    pass
            else:
                print("this didn't work")
        k = max(avgyearpreciplist[y])
        maxlist.append(k)    
            


    #print(avgyearpreciplist)
lowestrainfall = min(minlist)
y = minlist.index(min(minlist))
print("The lowest rainfall recorded was " + str(lowestrainfall)+" inches.")
print("This site had the lowest rainfall: "+ file_nametuple[y])
b = min(minlist)
print(y)
print(b)
r = avgyearpreciplist[y+1].index(float(b))
print("This occurred in the year: " + yearnameslist[r])
maxrainfall = max(maxlist)
l = maxlist.index(max(maxlist))
z = avgyearpreciplist[l].index(float(maxrainfall))
print("The highest rainfall recorded was " + str(maxrainfall)+" inches.")
print("This site had the highest rainfall: " + file_nametuple[l])
print("This occurred in the year: " + yearnameslist[z])

print("finished program")





