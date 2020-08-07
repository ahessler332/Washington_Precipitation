import Precip_year_breakdown
from Precip_file_list import station
def weather_calc_year():
        """
        calculates the avg precipitation per year
        """
        yearcounter = 0
        for k in range(len(Precip_year_breakdown.yearbreakdown(station))):
            
            if len(Precip_year_breakdown.yearbreakdown(station)[k]) > 1:
                yearcounter = yearcounter + 1
            else:
                pass
        x = yearcounter
        avgyearprecip = []
        precipitation = 0
        t = len(Precip_year_breakdown.yearbreakdown(station))
        for y in range(t):
             for k in range(len(Precip_year_breakdown.yearbreakdown(station)[y])):
                precipitation = precipitation + Precip_year_breakdown.yearbreakdown(station)[y][k].get("precip")
                
             
             avgyearprecip.append(precipitation)
             
             precipitation = 0
             
        
        return avgyearprecip
print("finished Precip_year_calc")