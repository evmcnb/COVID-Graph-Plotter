import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
#import datetime
import grab
import json
import pandas as pd
import traceback

regions = ["nation", "region", "nhsRegion", "utla", "ltla"]

def submit():

    num = 0
    areaName = ["","","",""]
    areaType = ["","","",""]
    txt = ent_title.get()
    metricName = combo_metric.get()

    #Error checking
    if metricName == "":
        messagebox.showerror("Select Metric", "Please select a metric from the drop-down menu")


    if ent_first_area.get() != "":
        num += 1
        areaName[num-1] = ent_first_area.get().upper()
        if combo_first_area.get() != "":
            areaType[num-1] = combo_first_area.get()

    if ent_second_area.get() != "":
        num += 1
        areaName[num-1] = ent_second_area.get().upper()
        if combo_second_area.get() != "":
            areaType[num-1] = combo_second_area.get()

    if ent_third_area.get() != "":
        num += 1
        areaName[num-1] = ent_third_area.get().upper()
        if combo_third_area.get() != "":
            areaType[num-1] = combo_third_area.get()

    if ent_fourth_area.get() != "":
        num += 1
        areaName[num-1] = ent_fourth_area.get().upper()
        if combo_fourth_area.get() != "":
            areaType[num-1] = combo_fourth_area.get()

    #Error Checking
    if num == 0: 
        messagebox.showerror("Enter Area", "Please enter at least one area to plot a graph")

    #Starts a loop to loop through the number of areas to compare
    for i in range(num): 

        #Gets the data from the API handling for errors
        try:
            rawData = grab.grabJSON(areaName=areaName[i], metricName=metricName, areaType=areaType[i])
        except Exception as e:
            try:
                rawData = grab.grabJSON(areaName=areaName[i], metricName=metricName)
            except Exception as e:
                messagebox.showerror("Request Error", "There was an error in retrieving data. Please check spelling and formatting of {0}. If this does not work it may be possible that the data of {1} does not exist for {0}".format(areaName[i], metricName))

        
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
    
def clear():
    ent_first_area.delete(0, tk.END)
    ent_second_area.delete(0, tk.END)
    ent_third_area.delete(0, tk.END)
    ent_fourth_area.delete(0, tk.END)
    ent_title.delete(0, tk.END)
    combo_metric.delete(0,tk.END)
    combo_first_area.delete(0,tk.END)
    combo_second_area.delete(0,tk.END)
    combo_third_area.delete(0,tk.END)
    combo_fourth_area.delete(0,tk.END)


# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("COVID Graph Plotter v1.3")
window.resizable(False,False)

# Create a new frame `frm_form` to contain the Label
# and Entry widgets for entering address information.
frm_form = tk.Frame(relief=tk.FLAT, borderwidth=3)
# Pack the frame into the window
frm_form.pack()

# Create the Label and Entry widgets for "First Area"
lbl_first_area = tk.Label(master=frm_form, text="First Area:")
ent_first_area = tk.Entry(master=frm_form, width=40)

combo_first_area = Combobox(master=frm_form, width=10)
combo_first_area["values"] = regions
# Use the grid geometry manager to place the Label and
# Entry widgets in the first and second columns of the
# first row of the grid
lbl_first_area.grid(row=0, column=0, sticky="e")
ent_first_area.grid(row=0, column=1)
combo_first_area.grid(row=0, column=2)

# Create the Label and Entry widgets for "Second Area"
lbl_second_area = tk.Label(master=frm_form, text="Second Area:")
ent_second_area = tk.Entry(master=frm_form, width=40)

combo_second_area = Combobox(master=frm_form, width=10)
combo_second_area["values"] = regions
combo_second_area.grid(row=1, column=2)
# Place the widgets in the second row of the grid
lbl_second_area.grid(row=1, column=0, sticky="e")
ent_second_area.grid(row=1, column=1)
combo_second_area.grid(row=1, column=2)

# Create the Label and Entry widgets for "Third Area"
lbl_third_area = tk.Label(master=frm_form, text="Third Area:")
ent_third_area = tk.Entry(master=frm_form, width=40)

combo_third_area = Combobox(master=frm_form, width=10)
combo_third_area["values"] = regions
combo_third_area.grid(row=2, column=2)
# Place the widgets in the third row of the grid
lbl_third_area.grid(row=2, column=0, sticky="e")
ent_third_area.grid(row=2, column=1)

# Create the Label and Entry widgets for "Fourth Area"
lbl_fourth_area = tk.Label(master=frm_form, text="Fourth Area:")
ent_fourth_area = tk.Entry(master=frm_form, width=40)

combo_fourth_area = Combobox(master=frm_form, width=10)
combo_fourth_area["values"] = regions
combo_fourth_area.grid(row=3, column=2)
# Place the widgets in the fourth row of the grid
lbl_fourth_area.grid(row=3, column=0, sticky=tk.E)
ent_fourth_area.grid(row=3, column=1)


# Create the Label and Entry widgets for "Metric"
lbl_metric = tk.Label(master=frm_form, text="Metric:")
combo_metric = Combobox(master=frm_form, width=38)

combo_metric['values'] = ("newCasesBySpecimenDateRollingRate",
"newCasesByPublishDate",
"cumCasesByPublishDate",
"cumCasesBySpecimenDateRate", 
"newCasesBySpecimenDate", 
"cumCasesBySpecimenDateRate", 
"cumCasesBySpecimenDate", 
"newAdmissions", 
"newAdmissionsRollingRate",
"cumAdmissions", 
"cumTestsByPublishDate", 
"newTestsByPublishDate", 
"covidOccupiedMVBeds", 
"hospitalCases", 
"plannedCapacityByPublishDate", 
"newDeaths28DaysByPublishDate", 
"cumDeaths28DaysByPublishDate", 
"cumDeaths28DaysByPublishDateRate", 
"newDeaths28DaysByDeathDate", 
"cumDeaths28DaysByDeathDate", 
"cumDeaths28DaysByDeathDateRate",
"alertLevel",
"newVirusTests",
"newVirusTestsRollingRate",
"transmissionRateMax",
"transmissionRateMin",
"newPillarOneTestsByPublishDate", 
"cumPillarOneTestsByPublishDate", 
"newPillarTwoTestsByPublishDate", 
"cumPillarTwoTestsByPublishDate", 
"newPillarThreeTestsByPublishDate", 
"cumPillarThreeTestsByPublishDate", 
"newPillarFourTestsByPublishDate", 
"cumPillarFourTestsByPublishDate")

# Place the widgets in the sixth row of the grid
lbl_metric.grid(row=5, column=0, sticky=tk.E)
combo_metric.grid(row=5, column=1, pady=10)


# Create the Label and Entry widgets for "Title"
lbl_title = tk.Label(master=frm_form, text="Title:")
ent_title = tk.Entry(master=frm_form, width=40)
# Place the widgets in the seventh row of the grid
lbl_title.grid(row=6, column=0, sticky=tk.E)
ent_title.grid(row=6, column=1)


# Create a new frame `frm_buttons` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Create the "Submit" button and pack it to the
# right side of `frm_buttons`
btn_submit = tk.Button(master=frm_buttons, text="Plot", command=submit)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Create the "Clear" button and pack it to the
# right side of `frm_buttons`
btn_clear = tk.Button(master=frm_buttons, text="Clear", command=clear)
btn_clear.pack(side=tk.RIGHT, ipadx=10)










# Start the application
window.mainloop()