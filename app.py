import datetime as dt
from telnetlib import SE

from flask import Flask, jsonify
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# SQLAlchemy setup
# Create the engine and reflect the database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Assign the reflected table (now class instances) to a variable
Measurement = Base.classes.measurement
Station = Base.classes.station

# Connect to the database
session = Session(engine)

# Flask setup
app = Flask(__name__)

@app.route('/')
def welcome():
    return (
        '''
        Welcome to the Climate Analysis API!<br/>
        Available Routes:<br/>
        /api/v1.0/precipitation<br/>
        /api/v1.0/stations<br/>
        /api/v1.0/tobs<br/>
        /api/v1.0/temp/start/end
        '''
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query the database for precipitation from the previous year
    precip = (session.query(Measurement.date, Measurement.prcp)
                     .filter(Measurement.date >= prev_year)
                     .all())
    precip = {date: prcp for date, prcp in precip}
    # Structure and return as JSON
    return jsonify(precip)

@app.route('/api/v1.0/stations')
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route('/api/v1.0/tobs')
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = (session.query(Measurement.tobs)
                      .filter(Measurement.station == 'USC00519281')
                      .filter(Measurement.date >= prev_year)
                      .all())
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route('/api/v1.0/temp/<start>')
@app.route('/api/v1.0/temp/<start>/<end>')
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs),
           func.avg(Measurement.tobs),
           func.max(Measurement.tobs)]

    if not end:
        results = (session.query(*sel)
                          .filter(Measurement.date >= start)
                          .all())
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    results = (session.query(*sel)
                      .filter(Measurement.date >= start)
                      .filter(Measurement.date <= end)
                      .all())
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
