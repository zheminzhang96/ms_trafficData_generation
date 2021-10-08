import datetime as dt
import pandas as pd
import numpy as np
from datetime import *
import string
import random
from random import seed
from random import randint

# *******CLEANING AND FORMATTING DATA**********
data = pd.read_csv('TrafficCountBook.csv')
# print(data.to_string())
# data_clean = data.drop(["Unamed: 15", "Unamed: 15", "Unamed: 15", "Unamed: 16", "Unamed: 17"], axis=1)
# data_clean = data.dropna()
data_clean = data.drop(labels=range(1378, 1998), axis=0)
# print(data_clean.shape)
data_clean = data_clean.drop(columns=data_clean.columns[11:23], axis=1)
data_clean = data_clean.dropna()
data_clean = data_clean.reset_index(drop=True)
data_clean['Date'] = pd.to_datetime(data_clean['Date'])
data_clean['AM Hour'] = pd.to_datetime(data_clean['AM Hour']).dt.time
data_clean['PM Hour'] = pd.to_datetime(data_clean['PM Hour']).dt.time
# print(data_clean.shape)
# print(data_clean.to_string())
df = pd.DataFrame(data_clean)
df = df.rename(columns={'Site ID': 'SiteID', 'On Road': 'OnRoad', 'Ref Road': 'RefRoad', 'AM Hour': 'AM_Hour',
                        'AM Volume': 'AM_Volume', 'PM Hour': 'PM_Hour', 'PM Volume': 'PM_Volume'})
dayofweek_array = df['Date'].dt.dayofweek
weekofyear_array = df['Date'].dt.isocalendar().week
# df.assign(dayofweek=df['Date'].dt.dayofweek)
df.insert(loc=2, column='weekofyear', value=weekofyear_array)
df.insert(loc=3, column='dayofweek', value=dayofweek_array)
#print(len(df))
#for i in range(0, len(df)):

# df.to_csv(r'C:\#Classes\CSE599\TrafficData\traffic_data_export.csv')   #export new .csv file

# print(df.to_string())
# print(dayofweek_array.to_string())
# print(weekofyear_array.to_string())

# dataTypeSeries = data_clean.dtypes
# print(dataTypeSeries)

# SELECTING 10 STREETS in N/S DIRECTION
ns_group1 = df[(df.OnRoad == '7th Ave')]
ns_group_later = df[(df.OnRoad == 'Central Ave') | (df.OnRoad == 'ScottSdale Rd') |
                    (df.OnRoad == '19th Ave') | (df.OnRoad == 'Dobson Rd') | (df.OnRoad == 'Alma School Rd') |
                    (df.OnRoad == '56th St') | (df.OnRoad == '56th St - Mesa') | (df.OnRoad == 'Arizona Ave') |
                    (df.OnRoad == 'Country Club Dr - Maricopa County')]
# print(ns_group1.to_string())
# SELECTING 10 STREETS in E/W DIRECTION
ew_group = df[(df.OnRoad == 'Baseline Rd') | (df.OnRoad == 'University Dr') | (df.OnRoad == 'Broadway Rd') |
              (df.OnRoad == 'McDowell Rd') | (df.OnRoad == 'Camelback Rd') | (df.OnRoad == 'Indian School Rd') |
              (df.OnRoad == 'Peoria Ave') | (df.OnRoad == 'Thomas Rd') | (df.OnRoad == 'Buckeye Rd') |
              (df.OnRoad == 'Yuma Rd')]
# print(ew_group.to_string())
group = pd.concat([ns_group1, ns_group_later, ew_group])
group = group.reset_index()
# print(group.to_string())
for i in range(0, len(group)):
    #print(group.iloc[i]['AM_Hour'])
    group.at[i, 'AM_Hour'] = group.iloc[i]['AM_Hour'].hour + group.iloc[i]['AM_Hour'].minute/60
print(group.to_string())

# def generation_7thAve():
#     df_gen = pd.DataFrame(columns=["OnRoad", "RefRoad", "Hour", "Volume"])
#     example = {'OnRoad':'7th Ave', 'RefRoad':'Carefree', 'Hour':'8:00', 'Volume':100}
#     df_gen = df_gen.append(example, ignore_index=True)
#     for i in range(5):
#         df_gen.loc[i] = ['7th Ave', 'Hill', '7:30', 123]
#     print(df_gen.to_string())
#     #dataTypeSeries = df_gen.dtypes
#     #print(dataTypeSeries)
# generation_7thAve()

def removeDuplicates(lst):
    return list(set([i for i in lst]))
group_fortuple = group[['OnRoad', 'RefRoad', 'Direction']]
road_tuple = []
for row in group_fortuple.itertuples(index=False):
    road_tuple.append(tuple(row))
    removeDuplicates(road_tuple)
#print(road_tuple)

def road_pattern(selection, start_t, end_t):
    #print(selection[0][0])
    new_record = {}
    rand_time = random.uniform(start_t, end_t)
    if selection[0][0] == "Baseline Rd":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 30) + 5 + (rand_time * 15))
        if start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 100) + 140 + (rand_time - 5) * 400)
            #print(est_volume)
        if start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("baseline if")
        #print(new_record)
    if selection[0][0] == "Broadway Rd":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 30) + 5 + (rand_time * 10))
        if start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 300) + 200 + (rand_time - 5) * 500)
        if start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 400) + 550 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("broadway if")
        #print(new_record)
    if selection[0][0] == "Buckeye Rd":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 0 + (rand_time * 10))
            #print("first if")
        if start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 40) + 30 + (rand_time - 5) * 50)
            #print(est_volume)
        if start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
            #print("second if")
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("Buckeye if")
        #print(new_record)
    if selection[0][0] == "Camelback Rd":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 1000) + 300 + (rand_time - 5) * 200)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("camelback if")
        #print(new_record)
    if selection[0][0] == "Indian School Rd":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            if selection[0][1] == "99th Ave":
                est_volume = int(randint(0, 500) + 500 + (rand_time - 5) * 400)
            if selection[0][1] == "107th Ave":
                est_volume = int(randint(0, 500) + 500 + (rand_time - 5) * 400)
            if selection[0][1] == "195th Ave":
                est_volume = int(randint(0, 500) + 500 + (rand_time - 5) * 400)
            if selection[0][1] == "El Mirage Rd":
                est_volume = int(randint(0, 500) + 500 + (rand_time - 5) * 400)
            if selection[0][1] == "355th Ave":
                est_volume = int(randint(0, 100) + 80 + (rand_time - 5) * 20)
            if selection[0][1] == "411th Ave":
                est_volume = int(randint(0, 100) + 80 + (rand_time - 5) * 20)
            if selection[0][1] == "Salome Hwy":
                est_volume = int(randint(0, 100) + 80 + (rand_time - 5) * 20)
            if selection[0][1] == "Wintersburg Rd":
                est_volume = int(randint(0, 100) + 80 + (rand_time - 5) * 20)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("indian school if")
    if selection[0][0] == "McDowell Rd":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 500) + 300 + (rand_time - 5) * 400)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("McDowell if")
    if selection[0][0] == "Peoria Ave":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 100) + 100 + (rand_time - 5) * 100)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("peoria if")
    if selection[0][0] == "Thomas Rd":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 50) + 30 + (rand_time - 5) * 20)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("thomas if")
    if selection[0][0] == "University Dr":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 400) + 300 + (rand_time - 5) * 100)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("university if")
    if selection[0][0] == "Yuma Rd":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 500) + 300 + (rand_time - 5) * 150)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("yuma if")
    if selection[0][0] == "7th Ave":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 80) + 120 + (rand_time - 5) * 200)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("7th if")
    if selection[0][0] == "19th Ave":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 30) + 20 + (rand_time - 5) * 10)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("19th if")
    if selection[0][0] == "56th St":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 150) + 100 + (rand_time - 5) * 80)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
    if selection[0][0] == "56th St - Mesa":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 100) + 50 + (rand_time - 5) * 50)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                          'Direction': selection[0][2], 'AM_Hour': rand_time,
                          'AM_Volume': est_volume}
        #print("56th if")
    if selection[0][0] == "Alma School Rd":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 500) + 500 + (rand_time - 5) * 250)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("alma if")
    if selection[0][0] == "Central Ave":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 50) + 30 + (rand_time - 5) * 20)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("central if")
    if selection[0][0] == "Country Club Dr - Maricopa County":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 80) + 80 + (rand_time - 5) * 50)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("country club if")
    if selection[0][0] == "Dobson Rd":
        est_volume = 0
        if start_t >= 0 and end_t < 5:
            est_volume = int(randint(0, 20) + 5 + (rand_time * 10))
        elif start_t >= 5 and end_t < 8:
            est_volume = int(randint(0, 80) + 50 + (rand_time - 5) * 40)
        elif start_t >= 8 and end_t < 12:
            est_volume = int(randint(0, 100) + 850 + (rand_time - 8) * -200)
        new_record = {'OnRoad': selection[0][0], 'RefRoad': selection[0][1],
                      'Direction': selection[0][2], 'AM_Hour': rand_time,
                      'AM_Volume': est_volume}
        #print("dobson if")
    #print(new_record)
    return new_record

def am_patter1(start_t, end_t):
    # time1 = datetime.strptime("5:00:00", "%H:%M:%S")
    # time1 = time1.time()
    df_sample1 = group[group['AM_Hour'].between(start_t, end_t)]
    df_sample1 = df_sample1[['OnRoad', 'RefRoad', 'Direction', 'AM_Hour', 'AM_Volume']]
    for i in range(100):
        random_select = random.sample(road_tuple, 1)
        #print(random_select[0])
        #random_select = ('56th St', 'Montgomery Rd', 'N')
        new_record = road_pattern(random_select, start_t, end_t)
        df_sample1 = df_sample1.append(new_record, ignore_index=True)
        df_sample1 = df_sample1.sort_values(by=['OnRoad', 'RefRoad'])
    #df_sample1 = df_sample1.sort_values(by=['OnRoad', 'RefRoad'])
    print(df_sample1.to_string())
    df_sample1.to_json('sample6_7.json', orient="records")

am_patter1(6, 7)
