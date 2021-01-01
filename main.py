import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
#import datetime
import grab
import json
import pandas as pd
import traceback


print("By Evan McNab - v1.2")
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

def main():

    num = 0
    
    #Sets the number of areas to compare to use in for loop with exception handling
    try:
        num = int(input("Enter number of areas to compare (4 max)>> "))
    except Exception as e:
        print("""Invalid Entry - Restart
        
        
        """)
        main()

    #If the number entered is too high give warning and set to maximum
    if num >= 5:
        print("Too many areas to compare - 4 is the maximum")
        num = 4

    #Selects the metric to graph with short cut for rate per 100k
    metricSelector = input("Metric name (for rate per 100k enter *)>> ")

    if metricSelector == "*":
        metricName = "newCasesBySpecimenDateRollingRate"
    else: 
        metricName = metricSelector

    areaName = []
    rawData = []

    #Starts a loop to loop through the number of areas to compare
    for i in range(num): 
        
        areaName.append(input("Enter area name {0}/{1} (exact)>> ".format(str(i+1),str(num))).upper())
        
        #Gets the data from the API handling for errors
        try:
            rawData = grab.grabJson(areaName[i], metricName)
        except Exception as e:
            print("""Invalid Entry - Restart
            
            
            """)
            main()
        

        #Formats the data to just dates and the metric
        formattedData = pd.DataFrame(rawData['data']).sort_values(by='date')

        datesOrdered = formattedData[formattedData["date"] > "2020-07-31"]
        dates = datesOrdered[["date"]]

        #Needed for plotting multiple areas on the same graph
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


    #datetoday = str(datetime.date.today())

    txt = input("Enter title>> ")

    #Gets the most recent date on the retrieved data
    updatedDate = str(dates["date"].iloc[-1])
    print(updatedDate)

    #Makes a nice label for common metric
    if metricName == "newCasesBySpecimenDateRollingRate":
        formattedMetricName = "Rate per 100,000"
    else:
        formattedMetricName = metricName


    plt.legend()
    plt.xlabel("Date (Updated: " + updatedDate + ")", fontsize = 12)
    plt.ylabel(formattedMetricName, fontsize = 12)
    plt.title(txt, fontsize=20)
    plt.show()


restart = "Y"

while restart == "Y":
    restart = ""
    main()
    restart = input("Plot another graph (Y/N)?>>").upper()




