import Precip_month_breakdown
import Precip_year_breakdown
import Precip_file_list
from Precip_file_list import station
def weather_calc_month():
        """
        calculates the avg precipitation per month
        """
        yearcounter = 0
        for k in range(len(Precip_year_breakdown.yearbreakdown(station))):
            
            if len(Precip_year_breakdown.yearbreakdown(station)[k]) > 1:
                yearcounter = yearcounter + 1
            else:
                pass
            
        x = yearcounter
        k=0
        y=0
        avgdayprecip = []
        avgmonthprecip = []
        
        precipitation = 0
        t = len(Precip_month_breakdown.monthbreakdown(station))
        for y in range(t):
            
            for k in range(len(Precip_month_breakdown.monthbreakdown(station)[y])):
                precipitation = precipitation + Precip_month_breakdown.monthbreakdown(station)[y][k].get("precip")
                
            precipavgday = precipitation / (len(Precip_month_breakdown.monthbreakdown(station)[y]))#returns average rainfall per day 
            precipavgmonth = precipitation / ((len(Precip_month_breakdown.monthbreakdown(station)[y]))/x)
            avgdayprecip.append(precipavgday)
            avgmonthprecip.append(precipavgmonth)
            
            
            precipitation  = 0
        return (avgdayprecip, avgmonthprecip)
print("Finished Precip_month_calc")



