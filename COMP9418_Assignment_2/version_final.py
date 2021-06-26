'''
COMP9418 Assignment 2
This file is the example code to show how the assignment will be tested.

Name:     zID:

Name:     zID:
'''

# Make division default to floating-point, saving confusion
from __future__ import division
from __future__ import print_function


# Allowed libraries 
import numpy as np
import pandas as pd

from collections import OrderedDict as odict

from tabulate import tabulate


data = pd.read_csv("data.csv")

#calculate the reliability of 
#the sensor i.e the number of times the sensor is predicting the correct values



cols_sensor = ['reliable_sensor1',	'reliable_sensor2',	'reliable_sensor3',	'reliable_sensor4',	'unreliable_sensor1',	'unreliable_sensor2',	'unreliable_sensor3',	'unreliable_sensor4']


groundTruth = ['r1',	'r2',	'r3',	'r4',	'r5',	'r6',	'r7',	'r8',	'r9',	'r10',	'r11',	'r12',	'r13',	'r14',	'r15',	'r16',	'r17',	'r18',	'r19',	'r20',	'r21',	'r22',	'r23',	'r24',	'r25',	'r26',	'r27',	'r28',	'r29',	'r30',	'r31',	'r32',	'r33',	'r34',	'r35',	'c1',	'c2',	'c3',	'c4',	'o1',	'outside']


reliable_sensors = {
    'reliable_sensor1' : 'r16',
    'reliable_sensor2' : 'r5',   
    'reliable_sensor3' : 'r25',
    'reliable_sensor4' : 'r31',
    }


un_reliable_sensor = {
    'unreliable_sensor1' : 'o1',
    'unreliable_sensor2' : 'c3',
    'unreliable_sensor3' : 'r1',
    'unreliable_sensor4' : 'r24',
    }

door_sensor = {
    'door_sensor1' : ['r8','r9'],
    'door_sensor2' : ['c1','c2'],
    'door_sensor3' : ['r26','r27'],
    'door_sensor4' : ['c4','r35'],
    }


#replace the motion and non_motion values with 1 and 0 respectivily
data = data.replace("motion",1)
data = data.replace("no motion",0)

#check the data after replacing the motion and no motion values with 0 and 1
#print(data.head())


#data to be used for calculating the reliability of 
#all the sensors against the ground truth

datat_reliability_cols = list(cols_sensor+groundTruth)


data_reliability = np.array(data[datat_reliability_cols])

#
#print(data_reliability[:5])

#use index func of list to find the index of the col you want in numpy


#creating the sensors list to use later
sensors = list(reliable_sensors.keys()) + list(un_reliable_sensor.keys())

#creating combined locations and sensors dict for latter use
combined_sensors_and_locations_dict = {**reliable_sensors,**un_reliable_sensor}

master_reliability_table = odict()


#print("sensors",sensors)
#pick the first column from cols_sensor
#and then find  that column in numpy and compare its value with the number of people in the room
for i in sensors:
    sensor_index = cols_sensor.index(i)
    
    #print(len(data_reliability[:,sensor_index]))
    
    sensor_col = data_reliability[:,sensor_index]
    
    # print("sensor_col")
    
    # print(pd.Series(sensor_col).head(25))
    
    
    #debugging
    # print(sensor_col[sensor_index])
    #print("i",i)
    #get the room name from the locations and sensors index
    room = combined_sensors_and_locations_dict[i]
    #print(room)
    
    #get the column of the ground truth for the sensor
    groundTruth_index = datat_reliability_cols.index(room)
    groundTruth_col = data_reliability[:,groundTruth_index]
    
    # print("groundTruth")
    
    # print(pd.Series(groundTruth_col).head(25))
    
    
    count_T = 0
    for k in range(0,len(sensor_col)):
       
        #if the k value of  both columns is equal to 1 then count it
        if sensor_col[k] == 1 and groundTruth_col[k] > 0:
            # print("k",k)
            # print('sensor_col',sensor_col[k])
            # print('ground_truth',groundTruth_col[k])
            count_T = count_T + 1
    
    #calculating the true prob
    total_num_values = len(sensor_col)
    
    # print(i)
    # print("count_T",count_T)
    # print("total",total_num_values)
    
    prob_T = count_T / total_num_values
    prob_F = 1 - prob_T
    
    #creating the probability table with dom and table
    sensor_reliability_prob_table = odict()
    
    sensor_reliability_prob_table['dom'] = tuple((i,))
    
    prob_table = odict()
    
    prob_table[tuple((True,))] = prob_T
    
    prob_table[tuple((False,))] = prob_F
    
    sensor_reliability_prob_table['table'] = prob_table
    
    master_reliability_table[i] = sensor_reliability_prob_table
#if the sensors  reading is motion and number of people is greater then zero. this is the number of
#correct predictions the sensor is making



#count the number of the total number of predictions which is equal to len of index of of the  sensor column

#divide the number of true predictions with total count. we call this the reliability of the sensor and store 

#it to with some value and if it is greater than a certain threshold then we will replace it in our next state


def printFactor(f):
    """
    argument 
    `f`, a factor to print on screen
    """
    # Create a empty list that we will fill in with the probability table entries
    table = list()
    
    # Iterate over all keys and probability values in the table
    for key, item in f['table'].items():
        # Convert the tuple to a list to be able to manipulate it
        k = list(key)
        # Append the probability value to the list with key values
        k.append(item)
        # Append an entire row to the table
        table.append(k)
    # dom is used as table header. We need it converted to list
    dom = list(f['dom'])
    # Append a 'Pr' to indicate the probabity column
    dom.append('Pr')
    print(tabulate(table,headers=dom,tablefmt='orgtbl'))


# printFactor(master_reliability_table['unreliable_sensor1'])

reliability_df = pd.DataFrame()


for i in master_reliability_table.keys():
    #print(master_reliability_table[i]['table'][(True,)])
    
    #create a series for a sensor
    col_values = []
    
    col_values.append(master_reliability_table[i]['table'][(True,)])
    
    col_values.append(master_reliability_table[i]['table'][(False,)])
    
    #print(pd.Series(col_values))
    
    #create the col using series
    
    reliability_df[i] = col_values
    
    
reliability_df.to_csv("reliability_sensors.csv")    

#print(reliability_df.head())
