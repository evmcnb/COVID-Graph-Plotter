# COVID-Graph-Plotter
~~~~~~For UK data only~~~~~~

# Description 

Allows instant plotting of data posted by the UK Government Coronavirus Dashboard: https://coronavirus.data.gov.uk/
A list of names of metrics and where in the hierarchy an area is: https://coronavirus.data.gov.uk/details/download

## Installation

Head on over to the release page for the latest version, or install the python source code and run `graph.py`

## Usage
```
Enter number of areas to compare (4 max)>>
```
This software allows comparison of a maxiumum of 4 different areas currently. So enter the number which you wish to compare

```
Metric name (for rate per 100k enter *)
```
For easy access to the Rate per 100,000 enter *. For all other metrics enter one of from the list of valid metirc names

<details>
  <summary>List of all valid metric names</summary>
  `newCasesByPublishDate` New cases by publish date
  `cumCasesByPublishDate` Cumulative cases by publish date
  `cumCasesBySpecimenDateRate` Rate of cumulative cases by publish date per 100k resident population
  `newCasesBySpecimenDate` New cases by specimen date
  `cumCasesBySpecimenDateRate` Rate of cumulative cases by specimen date per 100k resident population
  `cumCasesBySpecimenDate` Cumulative cases by specimen date
  `maleCases` Male cases (by age)
  `femaleCases` Female cases (by age)
  `newPillarOneTestsByPublishDate` New pillar one tests by publish date
  `cumPillarOneTestsByPublishDate` Cumulative pillar one tests by publish date
  `newPillarTwoTestsByPublishDate` New pillar two tests by publish date
  `cumPillarTwoTestsByPublishDate`Cumulative pillar two tests by publish date
  `newPillarThreeTestsByPublishDate` New pillar three tests by publish date
  `cumPillarThreeTestsByPublishDate` Cumulative pillar three tests by publish date 
  `newPillarFourTestsByPublishDate` New pillar four tests by publish date
  `cumPillarFourTestsByPublishDate` Cumulative pillar four tests by publish date
  `newAdmissions` New admissions
  `cumAdmissions`Cumulative number of admissions
  `cumAdmissionsByAge` Cumulative admissions by age
  `cumTestsByPublishDate` Cumulative tests by publish date
  `newTestsByPublishDate` New tests by publish date
  `covidOccupiedMVBeds` COVID-19 occupied beds with mechanical ventilators
  `hospitalCases` Hospital cases
  `plannedCapacityByPublishDate` Planned capacity by publish date
  `newDeaths28DaysByPublishDate` Deaths within 28 days of positive test
  `cumDeaths28DaysByPublishDate` Cumulative deaths within 28 days of positive test
  `cumDeaths28DaysByPublishDateRate` Rate of cumulative deaths within 28 days of positive test per 100k resident population
  `newDeaths28DaysByDeathDate` Deaths within 28 days of positive test by death date
  `cumDeaths28DaysByDeathDate` Cumulative deaths within 28 days of positive test by death date
  `cumDeaths28DaysByDeathDateRate`Rate of cumulative deaths within 28 days of positive test by death date per 100k resident population
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