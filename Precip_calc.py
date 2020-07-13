from prettytable import PrettyTable

monthnameslist = ["january" , "febuary", "march", "april", "may",
             "june", "july", "august", "september", "october",
             "november", "december"]
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
    def weather_calc():
        """
        calculates the avg precipitation per month
        """
        x = 25
        k=0
        y=0
        avgdayprecip = []
        avgmonthprecip = []
        precipitation = 0
        t = len(monthbreakdown(station))
        for y in range(t):
            
            for k in range(len(monthbreakdown(station)[y])):
                precipitation = precipitation + monthbreakdown(station)[y][k].get("precip")
                
            precipavgday = precipitation / (len(monthbreakdown(station)[y]))#returns average rainfall per day in january
            precipavgmonth = precipitation / ((len(monthbreakdown(station)[y]))/x)
            avgdayprecip.append(precipavgday)
            avgmonthprecip.append(precipavgmonth)
            
            
            precipitation  = 0
        return (avgdayprecip, avgmonthprecip)      



    weather_file(file_nametuple)

    monthbreakdown(station)

    #print("completed weather calculations")
    avgdayprecip = weather_calc()[0]
    avgdaypreciplist = []
    avgdaypreciplist.append(avgdayprecip)
    print("finished first calc")
    avgmonthprecip = weather_calc()[1]
    avgmonthpreciplist = []
    avgmonthpreciplist.append(avgmonthprecip)
    print("finished second calc")
    


    t = PrettyTable()
    t.field_names = ["months", "precipitation per day", "precipitation per month"]
    for k in range(12):
        t.add_row([monthnameslist[k], avgdayprecip[k], avgmonthprecip[k]]) 
    print(t)
    
    avgdayprecip = []
    avgmonthprecip = []
    monthlist = []
    record = {}
    station = []
    print("finished "+file_nametuple[q])
    

print("finished program")
