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


###################################
# Code stub
# 
# The only requirement of this file is that is must contain a function called get_action,
# and that function must take sensor_data as an argument, and return an actions_dict
# 

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

locations_and_sensors = {**reliable_sensors,**un_reliable_sensor,**door_sensor}

non_door_sensors = {**reliable_sensors,**un_reliable_sensor}



start_states = np.zeros((1,41),dtype='float')


rooms_and_columns = ['r1',	'r2',	'r3',	'r4',	'r5',	'r6',	'r7',	'r8',	'r9',	'r10',	'r11',	'r12',	'r13',	'r14',	'r15',	'r16',	'r17',	'r18',	'r19',	'r20',	'r21',	'r22',	'r23',	'r24',	'r25',	'r26',	'r27',	'r28',	'r29',	'r30',	'r31',	'r32',	'r33',	'r34',	'r35',	'c1',	'c2',	'c3',	'c4',	'o1',	'outside']

#setting the value of outside to 1.
start_states[0][40] = 1.0




# this global state variable demonstrates how to keep track of information over multiple 
# calls to get_action 
state = start_states.copy()

previous_state = state.copy()

#print("state",state)

# params = pd.read_csv(...)


count_T = 0



def get_action(sensor_data):
    # declare state as a global variable so it can be read and modified within this function
    global state
    global previous_state
    global reliable_sensors
    global un_reliable_sensor
    global door_sensor
    global locations_and_sensors
    global non_door_sensors
    global rooms_and_columns
    global count_T
    global transition_matrix_np
    
    #global params 
    
    actions_dict = {'lights1': 'off', 'lights2': 'on', 'lights3': 'off', 'lights4': 'off', 'lights5': 'off', 'lights6': 'off', 'lights7': 'off', 'lights8': 'off', 'lights9': 'off', 'lights10': 'off', 'lights11': 'off', 'lights12': 'off', 'lights13': 'off', 'lights14': 'off', 'lights15': 'off', 'lights16': 'off', 'lights17': 'off', 'lights18': 'off', 'lights19': 'off', 'lights20': 'off', 'lights21': 'off', 'lights22': 'off', 'lights23': 'off', 'lights24': 'off', 'lights25': 'off', 'lights26': 'off', 'lights27': 'off', 'lights28': 'off', 'lights29': 'off', 'lights30': 'off', 'lights31': 'off', 'lights32': 'off', 'lights33': 'off', 'lights34': 'off', 'lights35':'on'}
    
    
    #def robots
    robots = ['robot1','robot2']
    threshold = 0.2
    
    
    # #reading the transition matrix csv
    # transition_matrix = pd.read_csv("file_333.csv")

    # trans_cols = [*transition_matrix.columns]
    
    # transition_matrix.drop(trans_cols[0],inplace=True,axis=1)
    
    
    # transition_matrix_np = np.array(transition_matrix)
    
    transition_matrix = pd.DataFrame()
    
    
    
    #change the transition matrix on the basis of time
    if count_T == 0:
        
        #reading the transition matrix csv
        transition_matrix = pd.read_csv("file_time_0.csv")
    
        trans_cols = [*transition_matrix.columns]
        
        transition_matrix.drop(trans_cols[0],inplace=True,axis=1)
        
        
        transition_matrix_np = np.array(transition_matrix)
        
        
        #change the transition matrix on the basis of time
        
    if count_T == 500:
        #reading the transition matrix csv
        transition_matrix = pd.read_csv("file_time_1.csv")
    
        trans_cols = [*transition_matrix.columns]
        
        transition_matrix.drop(trans_cols[0],inplace=True,axis=1)
        
        
        transition_matrix_np = np.array(transition_matrix)
        
    if count_T == 1000:
         #reading the transition matrix csv
        transition_matrix = pd.read_csv("file_time_2.csv")
    
        trans_cols = [*transition_matrix.columns]
        
        transition_matrix.drop(trans_cols[0],inplace=True,axis=1)
        
        
        transition_matrix_np = np.array(transition_matrix)
    
    if count_T == 1500:
         #reading the transition matrix csv
        transition_matrix = pd.read_csv("file_time_3.csv")
    
        trans_cols = [*transition_matrix.columns]
        
        transition_matrix.drop(trans_cols[0],inplace=True,axis=1)
        
        
        transition_matrix_np = np.array(transition_matrix)
        
    if count_T == 2000:
         #reading the transition matrix csv
        transition_matrix = pd.read_csv("file_time_4.csv")
    
        trans_cols = [*transition_matrix.columns]
        
        transition_matrix.drop(trans_cols[0],inplace=True,axis=1)
        
        
        transition_matrix_np = np.array(transition_matrix) 
        
        
        
        transition_matrix_np = np.array(transition_matrix)   
    
    
    #reading the reliiabilities of the sensors
    reliability_sensors_df = pd.read_csv("reliability_sensors.csv")
    
    reliability_cols = [*reliability_sensors_df.columns]
    
    reliability_sensors_df.drop(reliability_cols[0],inplace=True,axis=1)
    
    
    reliability_sensors_np = np.array(reliability_sensors_df)
    
    

    
    
    #changing the sensor data
    #motion to True and no motion to False
    
    #print(sensor_data)
    
    for k,v in sensor_data.items():
        if k in locations_and_sensors.keys():
            if v == "motion":
                sensor_data[k] = 1
            else:
                sensor_data[k] = 0
    
    
    for i in non_door_sensors.keys():
        #print("i",i)
        #print("sensor_data",sensor_data[i])
        
        if i in non_door_sensors.keys() and sensor_data[i] != None:
        
            #matrix multiplication of start state with transition matrix
            state = previous_state @ transition_matrix_np
            
            #print(state)
            
            #setting the robot values in the state
        elif i in non_door_sensors.keys() and sensor_data[i] == None:
            
            room = non_door_sensors[i]
            
            room_index = rooms_and_columns.index(room)
            
            state[room_index] = 0.0

            #matrix multiplication of start state with transition matrix
            state = previous_state @ transition_matrix_np
            
    
    #getting those values
    for r in robots:
        if sensor_data[r] != None:
            sensor_room = sensor_data[r].split(',')[0].strip('(')
            num_of_people = sensor_data[r].split(',')[1].strip(')')
           
            sensor_room = sensor_room.strip("'")
            
            sensor_room_index = rooms_and_columns.index(sensor_room)
            
            #print(sensor_room_index)
            
            if sensor_room.startswith('r'):
                state[0][sensor_room_index] = num_of_people
    
    #setting value of the reliability of the sensors
    
    #find the diff of the curr state and the previous and if that difference is less than a threshold
    #replace these values
    
    #print(state)
                
   
                
    for i in non_door_sensors.keys():
        #print("i",i)
        
        room = non_door_sensors[i]
        
        #print('room',room)
        
        room_index = rooms_and_columns.index(room)
        
        #print('room_index',room_index)
        
        sensor_index_list = [*non_door_sensors]
        
        #print('sensor_index_list',sensor_index_list)
        
        sensor_index = sensor_index_list.index(i)
        
        #print("sensor_index",sensor_index)
        
        sensor_value = reliability_sensors_np[0][sensor_index]
        
        if (previous_state[0][room_index]) - (state[0][room_index]) < threshold:
            state[0][room_index] = sensor_value    
    
    count = 0
    
    #confrim about prediction
    for i in actions_dict.keys():
        
        # print("####################")
        # print(state[0][count]*10)
        # print("------------------------")
        
        # print(previous_state[0][count])
        # print("#######################")
        
        if state[0][count]*10 > 1.43:
            actions_dict[i] = "on"
        else:
            actions_dict[i] = "off"
        
        count = count + 1
        
    #print(state)
     
        
   
    
    
    count_T = count_T + 1
    previous_state = state
    
    # TODO: Add code to generate your chosen actions, using the current state and sensor_data

    
    return actions_dict



