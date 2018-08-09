import pickle
import pandas as pd
import numpy as np

# read in the model
mc_model= pickle.load(open("savelogreg.p","rb"))


# create a function to take in user-entered amounts and apply the model
def flight_delay(lesdonnees, model=mc_model):

    # put everything in terms of tablespoons
    # flour, milk, sugar, butter, eggs, baking powder, vanilla, salt
    #multipliers = [16, 16, 16, 16, 3, .33, .33, .33]

    # sum up the total values to get the total number of tablespoons in the batter
    #total = np.dot(multipliers, amounts_float)

    # note the proportion of flour and sugar
    #flour_cups_prop = multipliers[0] * amounts_float[0] * 100.0 / total
    #sugar_cups_prop = multipliers[2] * amounts_float[2] * 100.0 / total

    # inputs into the model
    #input_df = [[flour_cups_prop, sugar_cups_prop]]

    quarter = 1
    month = 6
    dayofmonth = 1
    dayofweek = 2
    airlineid = 19805
    flightnum = 447
    originairportid = 30977
    origincitymarketid = 33244
    originstatefips = 47
    destairportid = 30466
    destcitymarketid = 31454
    deststatefips = 12
    crsdeptime = 1350
    deptime = 1353
    depdelay = int(lesdonnees[2])
    depdelayminutes = 3.0
    depdel15 = 0.0
    departuredelaygroups = 0.0
    crsarrtime = 1650
    arrtime = 1700.0
    cancelled = 0.0
    airtime = 109.0
    flights = 1.0
    distance = int(lesdonnees[6])
    distancegroup = 3
    mfr_year = 2009
    serial_number = 36641.0


    input_df = [[quarter,
                    month,
                    dayofmonth,
                    dayofweek,
                    airlineid,
                    flightnum,
                    originairportid,
                    origincitymarketid,
                    originstatefips,
                    destairportid,
                    destcitymarketid,
                    deststatefips,
                    crsdeptime,
                    deptime,
                    depdelay,
                    depdelayminutes,
                    depdel15,
                    departuredelaygroups,
                    crsarrtime,
                    arrtime,
                    cancelled,
                    airtime,
                    flights,
                    distance,
                    distancegroup,
                    mfr_year,
                    serial_number]]

    # make a prediction
    prediction = int(mc_model.predict(input_df)[0])

    # return a message
    message_array = ["You will be on-time",
                    "You will be delayed"]

    return message_array[prediction]
