# import dependencies
import datetime as dt
import numpy as np
import pandas as pd

# import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import flask dependencies
from flask import Flask, jsonify



# set up the database
# set up engine to access and query SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create variables for each class
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database
session = Session(engine)



# Set up Flask
# define Flask app
app = Flask(__name__)

# define welcome route
@app.route("/")

# add routing info for all other routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')




# create precipitation route
@app.route("/api/v1.0/precipitation")

# create precipitation() function
def precipitation():
    # calculate the previous year
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    
    # jsonify data
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
    



# create stations route
@app.route("/api/v1.0/stations")

# create stations() function
def stations():
    results = session.query(Station.station).all()

    # unravel our results into a one-dimensional array and convert to a list
    stations = list(np.ravel(results))
    # jsonify results
    return jsonify(stations=stations)




# create temperature observations route
@app.route("/api/v1.0/tobs")

# create temp observations function
def temp_monthly():
    # calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == "USC00519281").\
        filter(Measurement.date >= prev_year).all()

    # unravel our results into a one-dimensional array and convert to a list
    temps = list(np.ravel(results))

    # jsonify results
    return jsonify(temps=temps)


# create stats route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# create a stats function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

