# COVID-Graph-Plotter

Allows instant plotting of data posted by the UK Government Coronavirus Dashboard: https://coronavirus.data.gov.uk/
A list of names of metrics and where in the hierarchy an area is: https://coronavirus.data.gov.uk/details/download

## Installation

Head on over to the release page for the latest version, or install the python source code and run `main.py`

Or to use an online version (v1.2.5): https://trinket.io/python3/9694673877?outputOnly=true&runOption=run

## Usage
### Entering the areas of Interest: 
```
First Area:
Second Area:
etc
```
This software allows comparison of a maxiumum of 4 different areas currently. So enter the names of the areas which you wish to compare.

To the side of this is a drop-down list of region types. This is **only** for use for some areas which appear under multiple categories. To spot this when plotted these regions will extend beyond others:

![alt text](https://imgur.com/oAHGd1S)
![alt text](https://imgur.com/DopVJRH)

Examples of these regions are Manchester and Camden. To fix this a region type needs to be specified (`utla` in this case):
![alt text](https://imgur.com/r5k2pmE)
![alt text](https://imgur.com/DMuzp48)

### Selecting metric 
```
Metric:
```
See a list of what most metric names mean below: 

<details>
  <summary>List of all valid metric names</summary>
	<code>newCasesByPublishDate</code> New cases by publish date <br />
  <code>cumCasesByPublishDate</code> Cumulative cases by publish date <br />
  <code>cumCasesBySpecimenDateRate</code> Rate of cumulative cases by publish date per 100k resident population <br />
  <code>newCasesBySpecimenDate</code> New cases by specimen date <br />
  <code>cumCasesBySpecimenDateRate</code> Rate of cumulative cases by specimen date per 100k resident population <br />
  <code>cumCasesBySpecimenDate</code> Cumulative cases by specimen date <br /> 
  <code>newPillarOneTestsByPublishDate</code> New pillar one tests by publish date <br /> 
  <code>cumPillarOneTestsByPublishDate</code> Cumulative pillar one tests by publish date <br />
  <code>newPillarTwoTestsByPublishDate</code> New pillar two tests by publish date <br />
  <code>cumPillarTwoTestsByPublishDate</code> Cumulative pillar two tests by publish date <br />
  <code>newPillarThreeTestsByPublishDate</code> New pillar three tests by publish date <br /> 
  <code>cumPillarThreeTestsByPublishDate</code> Cumulative pillar three tests by publish date <br /> 
  <code>newPillarFourTestsByPublishDate</code> New pillar four tests by publish date <br /> 
  <code>cumPillarFourTestsByPublishDate</code> Cumulative pillar four tests by publish date <br />
  <code>newAdmissions</code> New admissions <br />
  <code>cumAdmissions</code> Cumulative number of admissions <br />
  <code>cumTestsByPublishDate</code> Cumulative tests by publish date <br />
  <code>newTestsByPublishDate</code> New tests by publish date <br />
  <code>covidOccupiedMVBeds</code> COVID-19 occupied beds with mechanical ventilators <br />
  <code>hospitalCases</code> Hospital cases <br /> 
  <code>plannedCapacityByPublishDate</code> Planned capacity by publish date <br />
  <code>newDeaths28DaysByPublishDate</code> Deaths within 28 days of positive test <br />
  <code>cumDeaths28DaysByPublishDate</code> Cumulative deaths within 28 days of positive test <br />
  <code>cumDeaths28DaysByPublishDateRate</code> Rate of cumulative deaths within 28 days of positive test per 100k resident population <br /> 
  <code>newDeaths28DaysByDeathDate</code> Deaths within 28 days of positive test by death date <br /> 
  <code>cumDeaths28DaysByDeathDate</code> Cumulative deaths within 28 days of positive test by death date <br /> 
  <code>cumDeaths28DaysByDeathDateRate</code> Rate of cumulative deaths within 28 days of positive test by death date per 100k resident population <br />
</details> 

### Plotting Graph
```
Title:
```
This will be the title of the graph shown so name it something useful!

After this click the plot button

## Dependancies
A list of dependancies and installation commands: 
* Matplotlib
```
python -m pip install -U matplotlib
```
* Pandas
```
pip install pandas
```
* UK Government COVID
```
pip install uk-covid19
```
