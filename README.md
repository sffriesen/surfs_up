# surfs_up

## Overview of the Analysis
This project is to analyze weather data using SQLite and SQLAlchemy, in order to determine if a surf & ice cream shop will be successful in Oahu, Hawaii. This particular dataset collects both temperature and precipitation data throughout the year (over several years). Here I am using temperature data from the months of June and December to help determine if the surf & ice cream shop would be sustainable year round.

## Results


According to the descriptive statistics generated from our DataFrame of temperature data (seen in the images below for June and December, respectively), we can see the following results:
![june_temps]
![dec_temps]
- Mean temperatures
  - June: 74.94 degrees
  - December: 71.04 degrees


- (Minimum/Maximum) temperatures
  - June: (64/85) degrees
  - December: (56/83) degrees


- Standard Deviation for temperatures
  - June: 3.26 degrees
  - December: 3.75 degrees

## Summary
high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December

The temperatures are actually quite similar between the dead of winter and height of summer (with the average temperatures only being 3-4 degrees apart). Since the standard deviation is a bit higher for December, we can conclude that the temperature varies more in the winter (we can also see this with the minimum and maximum temperature for December varying a whole 27 degrees).

We could also query precipitation data for June and December to see if rain becomes an issue in the winter months. To do this we could build a query such as this:

`
`

Another option would be to 
