# COVID-Graph-Plotter

# Description 

Allows instant plotting of data posted by the UK Government Coronavirus Dashboard: https://coronavirus.data.gov.uk/
A list of names of metrics and where in the hierarchy an area is: https://coronavirus.data.gov.uk/details/download

## Installation

Head on over to the release page for the latest version, or install the python source code and run `graph.py`

## Usage
After running the program the following prompts will appear: 
```
Enter number of areas to compare (4 max)
```
This software allows comparison of a maxiumum of 4 different areas currently. So enter the number which you wish to compare

```
Metric name (for rate per 100k enter *)
```
For easy access to the Rate per 100,000 enter *. For all other metrics enter one of from the list of valid metirc names

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

```
Enter the number of the area type 
```
For this you need to know what level the area of interest is. For example if I wanted to plot England I would enter 2, as England is a nation. If I wanted to plot Essex I would enter 5 as it is a county (upper-tier local authority)

```
Enter area name (exact)
```
Enter the name of the area that you are interested in. To continue the above examples, for England enter `England` and for Essex enter `Essex`.

These steps then repeat for as many areas as you wish to compare.

Once this has finished the final prompt will be shown:
```
Enter title
```
This will be the title of the graph shown so name it something useful!

After this a graph will be shown of the output.

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
