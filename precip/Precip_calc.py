from prettytable import PrettyTable

monthnameslist = ["january" , "febuary", "march", "april", "may",
             "june", "july", "august", "september", "october",
             "november", "december"]

yearnameslist = ["1988","1989","1990","1991","1992","1993","1994",
                 "1995","1996","1997","1998","1999","2000","2001",
                 "2002","2003","2004","2005","2006","2007","2008",
                 "2009","2010","2011","2012","2013","2014","2015",
                 "2016","2017","2018","2019","2020"]
dictlist = []

dictlist.append("site number")
dictlist.append("date")
dictlist.append("precip")
dictlist.append("condition")

station = []

file_nametuple =("Hydrology_Fall_City.csv","Hydrology_Federal_Way.csv",
                "Hydrology_Bothell.csv", "Hydrology_North_Vashon.csv",
                "Hydrology_South_Vashon.csv", "Hydrology_Mukilteo.csv",
                "Hydrology_Bellevue.csv", "Hydrology_Burien.csv",
                "Hydrology_Cougar_MT.csv", "Hydrology_Enumclaw.csv")
        


z = len(file_nametuple)
avgyearpreciplist = []
avgdaypreciplist = []
avgmonthpreciplist = []

for q in range(z):  
    
    def weather_file(file_nametuple):
        """Takes weather data csv file and reads it
           into a dictionary and appended to a list 
        """
        file_name = file_nametuple[q]
        
        with open(file_name,'r') as file:
            next(file)
            for line in file:
                line = line.strip('\n')
                line_list = line.split(",")
                
                record = {}
                
                record[dictlist[1]] = str(line_list[1])
                
                record[dictlist[2]] = float(line_list[2])
                
                record[dictlist[3]] = str(line_list[3])
                
                station.append(record)
        return station       
            

    def monthbreakdown(station):
        """ creates list of months and breaks down data between months

        """
        x = len(station)
        
        monthlist = []
        januarylist = []
        febuarylist = []
        marchlist = []
        aprillist = []
        maylist = []
        junelist = []
        julylist = []
        augustlist = []
        septemberlist = []
        octoberlist = []
        novemberlist = []
        decemberlist = []
        monthlist.append(januarylist)
        monthlist.append(febuarylist)
        monthlist.append(marchlist)
        monthlist.append(aprillist)
        monthlist.append(maylist)
        monthlist.append(junelist)
        monthlist.append(julylist)
        monthlist.append(augustlist)
        monthlist.append(septemberlist)
        monthlist.append(octoberlist)
        monthlist.append(novemberlist)
        monthlist.append(decemberlist)   
        
        for k in range(x):
            date = station[k].get("date")
            date = date.split("/")
            if "2020" in date[2]:
                pass
            elif "12" in date[0]:
                monthlist[11].append(station[k])
            elif "2" in date[0]:
                monthlist[1].append(station[k])
            elif "3" in date[0]:
                monthlist[2].append(station[k])
            elif "4" in date[0]:
                monthlist[3].append(station[k])
            elif "5" in date[0]:
                monthlist[4].append(station[k])
            elif "6" in date[0]:
                monthlist[5].append(station[k])
            elif "7" in date[0]:
                monthlist[6].append(station[k])
            elif "8" in date[0]:
                monthlist[7].append(station[k])
            elif "9" in date[0]:
                monthlist[8].append(station[k])
            elif "10" in date[0]:
                monthlist[9].append(station[k])
            elif "11" in date[0]:
                monthlist[10].append(station[k])
            else: 
                monthlist[0].append(station[k])
         
        
        
        
        return monthlist
        
    #perhaps break it down to separate functions for each month
    def yearbreakdown(station):
        """
            Break down data year by year basis
        """
        x = len(station)
        yearlist = []
        nineteen88 = []
        nineteen89 = []
        nineteen90 = []
        nineteen91 = []
        nineteen92 = []
        nineteen93 = []
        nineteen94 = []
        nineteen95 = []
        nineteen96 = []
        nineteen97 = []
        nineteen98 = []
        nineteen99 = []
        two000 = []
        two001 = []
        two002 = []
        two003 = []
        two004 = []
        two005 = []
        two006 = []
        two007 = []
        two008 = []
        two009 = []
        two010 = []
        two011 = []
        two012 = []
        two013 = []
        two014 = []
        two015 = []
        two016 = []
        two017 = []
        two018 = []
        two019 = []
        two020 = []
        yearlist.extend((nineteen88,nineteen89,nineteen90,nineteen91,
                        nineteen92,nineteen93,nineteen94,nineteen95,
                        nineteen96,nineteen97,nineteen98,nineteen99,
                        two000,two001,two002,two003,two004,two005,
                        two006,two007,two008,two009,two010,two011,
                        two012,two013,two014,two015,two016,two017,
                        two018,two019,two020))
        for k in range(x):
            date = station[k].get("date")
            date = date.split("/")
            if "2020" in date[2]:
                yearlist[32].append(station[k])
            elif "1988" in date[2]:
                yearlist[0].append(station[k])
            elif "1989" in date[2]:
                yearlist[1].append(station[k])
            elif "1990" in date[2]:
                yearlist[2].append(station[k])
            elif "1991" in date[2]:
                yearlist[3].append(station[k])
            elif "1992" in date[2]:
                yearlist[4].append(station[k])
            elif "1993" in date[2]:
                yearlist[5].append(station[k])
            elif "1994" in date[2]:
                yearlist[6].append(station[k])
            elif "1995" in date[2]:
                yearlist[7].append(station[k])
            elif "1996" in date[2]:
                yearlist[8].append(station[k])
            elif "1997" in date[2]:
                yearlist[9].append(station[k])
            elif "1998" in date[2]:
                yearlist[10].append(station[k])
            elif "1999" in date[2]: 
                yearlist[11].append(station[k])
            elif "2000" in date[2]:
                yearlist[12].append(station[k])
            elif "2001" in date[2]:
                yearlist[13].append(station[k])
            elif "2002" in date[2]:
                yearlist[14].append(station[k])
            elif "2003" in date[2]:
                yearlist[15].append(station[k])
            elif "2004" in date[2]:
                yearlist[16].append(station[k])
            elif "2005" in date[2]:
                yearlist[17].append(station[k])
            elif "2006" in date[2]:
                yearlist[18].append(station[k])
            elif "2007" in date[2]:
                yearlist[19].append(station[k])
            elif "2008" in date[2]:
                yearlist[20].append(station[k])
            elif "2009" in date[2]:
                yearlist[21].append(station[k])
            elif "2010" in date[2]:
                yearlist[22].append(station[k])
            elif "2011" in date[2]:
                yearlist[23].append(station[k])
            elif "2012" in date[2]:
                yearlist[24].append(station[k])
            elif "2013" in date[2]:
                yearlist[25].append(station[k])
            elif "2014" in date[2]:
                yearlist[26].append(station[k])
            elif "2015" in date[2]:
                yearlist[27].append(station[k])
            elif "2016" in date[2]:
                yearlist[28].append(station[k])
            elif "2017" in date[2]:
                yearlist[29].append(station[k])
            elif "2018" in date[2]:
                yearlist[30].append(station[k])
            else :
                yearlist[31].append(station[k])
                
            
        return yearlist
        
    def weather_calc_year():
        """
        calculates the avg precipitation per year
        """
        yearcounter = 0
        for k in range(len(yearbreakdown(station))):
            
            if len(yearbreakdown(station)[k]) > 1:
                yearcounter = yearcounter + 1
            else:
                pass
        x = yearcounter
        avgyearprecip = []
        precipitation = 0
        t = len(yearbreakdown(station))
        for y in range(t):
             for k in range(len(yearbreakdown(station)[y])):
                precipitation = precipitation + yearbreakdown(station)[y][k].get("precip")
                

             
             avgyearprecip.append(precipitation)
             
             precipitation = 0
             
        
        return avgyearprecip
            
    def weather_calc_month():
        """
        calculates the avg precipitation per month
        """
        yearcounter = 0
        for k in range(len(yearbreakdown(station))):
            
            if len(yearbreakdown(station)[k]) > 1:
                yearcounter = yearcounter + 1
            else:
                pass
            
        x = yearcounter
        k=0
        y=0
        avgdayprecip = []
        avgmonthprecip = []
        
        precipitation = 0
        t = len(monthbreakdown(station))
        for y in range(t):
            
            for k in range(len(monthbreakdown(station)[y])):
                precipitation = precipitation + monthbreakdown(station)[y][k].get("precip")
                
            precipavgday = precipitation / (len(monthbreakdown(station)[y]))#returns average rainfall per day 
            precipavgmonth = precipitation / ((len(monthbreakdown(station)[y]))/x)
            avgdayprecip.append(precipavgday)
            avgmonthprecip.append(precipavgmonth)
            
            
            precipitation  = 0
        return (avgdayprecip, avgmonthprecip)      



    weather_file(file_nametuple)

    monthbreakdown(station)
    yearbreakdown(station)

    #print("completed weather calculations")
    avgdayprecip = weather_calc_month()[0]

    
    avgdaypreciplist.append(avgdayprecip)
    print("finished first calc")
    avgmonthprecip = weather_calc_month()[1]
    
    avgmonthpreciplist.append(avgmonthprecip)
    print("finished second calc")
    avgyearprecip = weather_calc_year()
    
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
