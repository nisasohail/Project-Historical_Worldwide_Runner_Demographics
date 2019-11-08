import os
import pandas as pd
import numpy as np
import sqlalchemy
import datetime as dt
import sqlite3 as sq
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

sql_data = 'db/rundata.sqlite'
conn = sq.connect(sql_data)
MenAge= pd.read_sql('select * from men_age_data', conn)
WomenAge = pd.read_sql('select * from women_age_data',conn)
GenderData = pd.read_sql('select * from gender_total_data',conn)
TotalData = pd.read_sql('select * from rundata',conn)
CombinedData = pd.read_sql('select * from combined_age_data',conn)
CountryEvent = pd.read_sql('select * from country_event_data',conn)


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/countryList")
def country_detail():
    df = CountryEvent
    data_ = {
        "country": df.Country
    }
    data=list(data_['country'].unique())
    return jsonify(data)

# for t in country_detail():
#     print(t, ": ", country_detail())

@app.route("/eventList")
def event_detail():
    df1 = TotalData
    data1 = {
        "event": df1.Event.unique().tolist()
    }
    return jsonify(data1)

@app.route("/genderList")
def gender_detail():
    gender = GenderData
    genderdata = {
        "gender": gender.Gender
    }
    gender_data=list(genderdata['gender'].unique())
    return jsonify(gender_data)

@app.route("/ageGroup")
def age_group():
    age = TotalData
    agegroup = {
        "agegroup": age.AgeGroup
    }
    age_group=list(agegroup['agegroup'].unique())
    return jsonify(age_group)

@app.route("/gender/<country>")
def gender_data(country):
    df2 = GenderData[GenderData['Country']==country]
    data2 = {
        "country": df2.Country.values.tolist(),
        "gender": df2.Gender.values.tolist(),
        "noOfAthletes":df2.Count.values.tolist()
    }
    return  jsonify(data2)
# print(gender_data())
# # for t in age_data():
# #     print(t,":",age_data())

@app.route("/event_detail/<country>")
def event_data(country):
    df3 = CountryEvent[(CountryEvent['Country']==country)]
    data3 = {
        "country": df3.Country.values.tolist(),
        "event": df3.Event.values.tolist(),
        "gender": df3.Gender.values.tolist(),
        "noOfAthletes":df3.Count.values.tolist()
    }

    return jsonify(data3)
    
@app.route("/agegroup/<country1>")
def agegroup_data(country1):
    df4 = CombinedData[CombinedData['Country']==country1]
    data4 = {
        "country": df4.Country.values.tolist(),
        "agegroup": df4.AgeGroup.values.tolist(),
        "gender": df4.Gender.values.tolist(),
        "noOfAthletes":df4.Count.values.tolist()
    }

    return jsonify(data4)

@app.route("/women/<agegroup>")
def womenagegroup_data(agegroup):
    df5 = WomenAge[WomenAge['AgeGroup']==agegroup]
    data5 = {
        "country": df5.Country.values.tolist(),
        "agegroup": df5.AgeGroup.values.tolist(),
        "noOfAthletes": df5.Count.values.tolist()
    }
    return jsonify(data5)

@app.route("/men/<country>")
def menagegroup_data(country):
    df6 = MenAge[MenAge['Country']==country]
    data6 = {
        "country": df6.Country.values.tolist(),
        "agegroup": df6.AgeGroup.values.tolist(),
        "noOfAthletes": df6.Count.values.tolist()
    }
    return jsonify(data6)

@app.route("/age/<country2>")
def age(country2):
    df7 = CombinedData[(CombinedData['Country']==country2) & (CombinedData['Gender']=='Men')]
    df8 = CombinedData[(CombinedData['Country']==country2) & (CombinedData['Gender']=='Women')]
    data4 = {
        "country": df7.Country.values.tolist(),
        "agegroup": df7.AgeGroup.values.tolist(),
        "gender": df7.Gender.values.tolist(),
        "mencount":df7.Count.values.tolist(),
        "womencount":df8.Count.values.tolist()
    }

    return jsonify(data4)

if __name__ == "__main__":
    app.run()