# **Surf Weather Analysis**

## **Overview of Project**
The goal of this project is to analyze a SQLite database of weather data from the island of Oahu using python tools such as SQLAlchemy and pandas. The results of interest are the statistics for temperature and precipitation in the months of June and December to get a feel for the differences between summer and winter in Hawaii. This exercise could serve as a first investigation into whether it would make sense to open a shop based on outdoor warm weather activities with the hope that it would be able to do well all year round.

The data has been gathered from nine weather stations across Oahu from January 2010 to August 2017. The result of SQLAlchemy reflection of the database reveals a measurement and station table with the following fields:

| Measurement | Station   |
| ----------- | --------- |
| id          | id        |
| station     | station   |
| date        | name      |
| prcp        | latitude  |
| tobs        | longitude |
|             | elevation |

The abbreviations *prcp* and *tobs* refer to precipitation in inches and temperature observations in degrees Fahrenheit respectively. All analysis is performed in the *[SurfsUp_Challenge.ipynb](/SurfsUp_Challenge.ipynb)* notebook.

>##### Note: Additional challenges are covered in the files *climate_analysis.ipynb* and *app.py* including creating a Flask application to display weather analysis results.

## **Analysis and Results**
There are two main deliverables for this project, one for each month of interest, that are detailed below.

### **Deliverable 1**
The first deliverable for this analysis is to produce a statistical summary of all the temperatures recorded in June. Using the SQLAlchemy `session.query()` method, temperature observations are first filtered by the extracted month value from the date field to leave just the data for June. Then the data is returned as a list of tuples via the `all()` method. Converting the result into a pandas DataFrame and using the `describe()` method yields the following:

<div align="center">
    <img src="Resources/jun_temps_df.svg"
         alt="June temperature stats" />
</div>

### **Deliverable 2**
The second deliverable is the same as the first with the month changed to December. Repeating the same steps as in deliverable 1, the results for temperatures in December are retrieved with the statistical summary as shown below:

<div align="center">
    <img src="Resources/dec_temps_df.svg"
         alt="December temperature stats" />
</div>

### **Comparing the Temperature Statistics**
The following observations are made using the two tables above:
- The average temperature for June is almost 4 degrees higher than in December. This is to be expected as June is a summer month whereas December is a winter month for Hawaii.
- As far as low temperatures go, December produced a minimum temperature 8 degrees lower than in June. On the opposite end of the spectrum, the maximums were only different by 2 degrees.
- For both distributions, the 25th and 75th percentiles are within one standard deviation of the mean


## **Summary**


<div align="center">
    <img src="Resources/avg_daily_temperature_scaled.svg"
         alt="Average Daily Temperature" />
</div>



<div align="center">
    <img src="Resources/avg_daily_precipitation_scaled.svg"
         alt="Average Daily Precipitation" />
</div>



<div align="center">
    <img src="Resources/prcp_stats_df.svg"
         alt="June and December Precipitation Stats" />
</div>