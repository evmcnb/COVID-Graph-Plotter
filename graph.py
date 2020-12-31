import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import datetime
import grab
import json
import pandas as pd

print("By Evan McNab - v1.1")
print(""" 
                 _____ ______      _______ _____    __  ___                    
                / ____/ __ \ \    / /_   _|  __ \  /_ |/ _ \                   
               | |   | |  | \ \  / /  | | | |  | |  | | (_) |                  
               | |   | |  | |\ \/ /   | | | |  | |  | |\__, |                  
               | |___| |__| | \  /   _| |_| |__| |  | |  / /                   
  _____       __\_____\____/  _\/__ |_____|_____/___|_|_/_/_____ ______ _____  
 |  __ \   /\|__   __|/\     |  __ \| |    / __ \__   __|__   __|  ____|  __ \ 
 | |  | | /  \  | |  /  \    | |__) | |   | |  | | | |     | |  | |__  | |__) |
 | |  | |/ /\ \ | | / /\ \   |  ___/| |   | |  | | | |     | |  |  __| |  _  / 
 | |__| / ____ \| |/ ____ \  | |    | |___| |__| | | |     | |  | |____| | \ \ 
 |_____/_/    \_\_/_/    \_\ |_|    |______\____/  |_|     |_|  |______|_|  \_\ 
 
 
 """)


num = int(input("Enter number of areas to compare (4 max)>> "))

metricSelector = input("Metric name (for rate per 100k enter *)>> ")

if metricSelector == "*":
    metricName = "newCasesBySpecimenDateRollingRate"
else: 
    metricName = metricSelector

areaType = []
areaName = []
rawData = []

for i in range(num): 
    print(""" 
          Enter the number of the area type {}:
              1 United Kingdom
              2 Nation
              3 Region
              4 NHS Region
              5 Upper-tier local Authority
              6 Lower-tier local Authority  
              """.format(str(i)))
              
    areaTypeSelector = int(input(">> "))
             
    
    if areaTypeSelector == 1:
        areaType.append("overview")
                  
    elif areaTypeSelector == 2:
        areaType.append("nation")
                      
    elif areaTypeSelector == 3:
        areaType.append("region")

    elif areaTypeSelector == 4:
        areaType.append("nhsRegion")
    
    elif areaTypeSelector == 5:
        areaType.append("utla")
    
    elif areaTypeSelector == 6:
        areaType.append("ltla")

    else: 
        print("Invalid Entry - Restart")
    
    areaName.append(input("Enter area name (exact)>> ").upper())


    rawData = grab.grabJson(areaType[i], areaName[i], metricName)
    formattedData = pd.DataFrame(rawData['data']).sort_values(by='date')

    datesOrdered = formattedData[formattedData["date"] > "2020-07-31"]
    dates = datesOrdered[["date"]]


    if i == 0:
        datesOrdered0 = datesOrdered
        a1 = datesOrdered0.plot(x="date", y="metric", label = areaName[i], figsize=(10,7))
    if i == 1:
        datesOrdered1 = datesOrdered
        a2 = datesOrdered1.plot(x="date", y="metric", label = areaName[i], figsize= (10,7), ax=a1)
    if i == 2:
        datesOrdered2 = datesOrdered
        a3 = datesOrdered2.plot(x="date", y="metric", label = areaName[i], figsize= (10,7), ax=a2)
    if i == 3:
        datesOrdered3 = datesOrdered
        a4 = datesOrdered3.plot(x="date", y="metric", label = areaName[i], figsize= (10,7), ax=a3)


datetoday = str(datetime.date.today())

#txt = "Rate of COVID-19 Cases in Ipswich Per 100,000"
txt = input("Enter title>> ")

print(dates["date"].iloc[-1])

if metricName == "newCasesBySpecimenDateRollingRate":
    formattedMetricName = "Rate per 100,000"
else:
    formattedMetricName = metricName


plt.legend()
plt.xlabel("Date", fontsize = 12)
plt.ylabel(formattedMetricName, fontsize = 12)
plt.title(txt, fontsize=20)
plt.show()


