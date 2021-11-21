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

```
dec_prec = session.query(Measurement.date, Measurement.prcp).\
            filter(func.strftime("%m", Measurement.date) == "12").all()

dec_prec_df = pd.DataFrame(dec_prec, columns = ["Date", "Precipitation"])
dec_prec_df.describe()
```
After doing the same for June, we can see the following summary statistics for June and December, respectively:

![june_prec]
![dec_prec]

Another option would be to look at the ratio of colder weather days in the winter months, such as December. To do this, we could query the December temperature data and add a filter to only look at days that fell below a certain temperature (that one might deem to be too cold for ice cream). We could do this using the following code (here I've used 60 degrees F as the filter):

```
# Query December days below 60 degrees F
cold_dec = session.query(Measurement.date, Measurement.tobs).\
            filter((func.strftime("%m", Measurement.date) == "12") & (Measurement.tobs < 60)).all()
cold_dec_df = pd.DataFrame(cold_dec, columns = ["Date", "Temperature"])
cold_dec_df.describe()
```

This gives us the following data and corresponding summary statistics:

![dec_cold_days]
![dec_cold_days_stats]

By dividing the count of "cold days" over total data points for days in December, only 0.4% of our December datapoints are under 60 degrees! Thus we can conclude that most days in December are relatively warm. This can be replicated for any temperature as well.
