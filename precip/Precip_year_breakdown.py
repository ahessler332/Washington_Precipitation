import Precip_file_list

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
print("Finished Precip_year_breakdown")    