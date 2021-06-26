#!/usr/bin/env python
# coding: utf-8

# In[916]:


#transition matrix for the markov model.

import pandas as pd
import numpy as np


# Dependencies for transition probabilities
previous_G = {
    'r1' : ['r2', 'r3','r4','r7'],
    'r2' : ['r1', 'r4','r3'],
    'r3' : ['r1', 'r7','r2'],
    'r4' : ['r2', 'r8'],
    'r5' : ['r6', 'r9', 'c3','r13'],
    'r6' : ['r5', 'c3','r9','r11'],
    'r7' : ['r3', 'c1','r1'],
    'r8' : ['r4', 'r9','r13','r5'],
    'r9' : ['r5', 'r8', 'r13'],
    'r10': ['c3','r11'],
    'r11': ['c3','r10'],
    'r12': ['r22', 'outside'],
    'r13': ['r9', 'r24','r8'],
    'r14': ['r24','r13'],
    'r15': ['c3','r11'],
    'r16': ['c3','r17'],
    'r17': ['c3','r16','r18'],
    'r18': ['c3','r17'],
    'r19': ['c3','r20'],
    'r20': ['c3','r19','r21'],
    'r21': ['c3','r20'],
    'r22': ['r12', 'r25','c1'],
    'r23': ['r24'],
    'r24': ['r13', 'r14', 'r23'],
    'r25': ['r22', 'r26','c1'],
    'r26': ['r25', 'r27','c1'],
    'r27': ['r26', 'r32'],
    'r28': ['c4','r35'],
    'r29': ['r30', 'c4'],
    'r30': ['r29','c4'],
    'r31': ['r32','r32'],
    'r32': ['r27', 'r31', 'r33'],
    'r33': ['r32'],
    'r34': ['c2','c4'],
    'r35': ['c4','r28'],
    'c1' : ['r7', 'r25', 'c2'],
    'c2' : ['r34', 'c1', 'c4'],
    'c3' : ['r5', 'r6', 'r10', 'r11', 'r15', 'r16', 'r17', 'r18', 'r19', 'r20', 'r21', 'o1'],
    'c4' : ['r28', 'r29', 'r35', 'c2', 'o1'],
    'o1' : ['c3', 'c4'],
    'outside': ['r12']
}


data = pd.read_csv("data.csv")


# In[919]:


data.columns


# In[920]:


temp_data = data[['r1', 'r2', 'r3', 'r4',
       'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15',
       'r16', 'r17', 'r18', 'r19', 'r20', 'r21', 'r22', 'r23', 'r24', 'r25',
       'r26', 'r27', 'r28', 'r29', 'r30', 'r31', 'r32', 'r33', 'r34', 'r35',
       'c1', 'c2', 'c3', 'c4', 'o1', 'outside']]


# In[921]:


# temp_data.head()


# In[922]:


# temp_data.head()


# In[923]:


# temp_data['r1'][0:20]


# In[ ]:





# In[924]:


transition = np.zeros((41,41),float)



#numpy conversion for the data frame
temp_numpy = temp_data.to_numpy()
#print(temp_numpy.shape)


# In[930]:


loop = 1

#location is prevoius location, col is column name

def check_val(col,loc,data,query_data):
    count = 0
    
    if data[loc+1][col] > data[loc][col]:
            count = data[loc+1][col] - data[loc][col]
    return count


#transition_check for the graph
def transition_check(count,loc,data,key,query_data):
    res = 0
    
    for trans in previous_G[key]:
        
        temp_trans = query_data.columns.get_loc(trans)
        
        res = check_val(temp_trans,loc,data,query_data)
        
        index_no = query_data.columns.get_loc(trans)
        row_val  = query_data.columns.get_loc(key)
        
        #row_val = [int(s) for key in str.split() if s.isdigit()]
        #index_no = [int(s) for trans in str.split() if s.isdigit()]
        
        if res > 0:
            transition[row_val][index_no]+=res
            return res
    #print(res)
    return res
        

transition = np.zeros((41,41),float)

begin = 0
end = 500

for iteration in range(5):
    
    time_data = temp_data[begin:end]
    time_numpy = time_data.to_numpy()
    
    for i in range(499):
    #print(i)
    
        for K in previous_G.keys():

            loc = time_data.columns.get_loc(K)

            if ( time_numpy[i][loc] > time_numpy[i+1][loc]):
                #print(temp_data['r1'].iloc[i])
                #print(i)
                #print("the value at " + str(i)+ "is :" + str(temp_data['r1'].iloc[i]))
                count = 0
                check_count = 0

                count = time_numpy[i][loc] - time_numpy[i+1][loc]

                if count > 0:
                    #print(check_count)
                    check_count = count


                output = transition_check(count,i,time_numpy,K,time_data)
                #print(ouput)
               # check_count-=ouput

                        #print(check_count)
                
    #pd.DataFrame(transition).to_csv("time_iteration" + "_"+ str(iteration)+ ".csv")
    
    #for the probability of motion
    
    temp_sum = time_data['r1'].sum()


    temp_num = np.true_divide(transition[0],temp_sum)


# print('temp_num',temp_num)


    transition[0,:] = temp_num[0:,]


# print(transition[0,:])



    for i in previous_G.keys():
        
        temp_sum = time_data[i].sum()+1
        
        loc = time_data.columns.get_loc(i)
        
        
        temp_num = np.true_divide(transition[loc],temp_sum)
        
        
        #print('temp_num',temp_num)
        
        
        transition[loc,:] = temp_num[0:,]
        
        
        #print(transition[0,:])
    
    for k in previous_G.keys():
        loc = temp_data.columns.get_loc(k)
        
        transition[loc][loc] = 1 - np.sum(transition[loc])
        #print(loc)
    pd.DataFrame(transition).to_csv("file_time_"+ str(iteration) + ".csv")