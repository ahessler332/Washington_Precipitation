#puts files into lists to work with

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

print("finished Precip_file_list")
