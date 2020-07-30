import Precip_file_list


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
print("finished Precip_month_breakdown")    