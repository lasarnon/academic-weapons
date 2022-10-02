# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 21:44:52 2022

@author: mille
"""

#6 The change in data collection may be due to law/policy introduced in 1989
#7 this format greatly reduces the storage space required to store data with repetitive descriptions
#8 Excel can't read unstructured data

f = open("US1969.dat", "r") 

counter = 0;
for x in f:
    if x[25] == "7" and x[26] == "4": # other conditions?
        counter = counter + 1
print(counter)


def isTexanBirth(x):
    if x[25] == "7" and x[26] == "4":
        return True
def isTexanMother(x):
    if (x[11]=="1" or x[11]=="2"):
        return True

f = open("US1969.dat", "r")
counter = 0;
for s in f:
    if isTexanBirth(s) and isTexanMother(s):
            counter = counter + 1
print(counter) 

""" 
10) The first code chunk counts live births in Texas (113310). 
    I made an assumption that conditions 1 and 2 in Tape Location 12 describe mothers who are residents of Texas.
    After defining the functions that filter data for borth live births in Texas and mothers who reside in Texas, the counter prints 112565. 
11) It makes sense that a very high percentage of births in Texas would be to mothers residing in Texas, 
    so I think I can be reasonably confident my assumption is a valid interpretation.
"""
import numpy as np
import matplotlib.pyplot as plt

G = np.zeros((3))

for x in f:
 #   print(x[96])
    if x[96] != '0' :
        if x[96] == '1' :
            G[0] += 1
        elif x[96] == '2' :
            G[1] += 1
        elif x[96] == '3' :
            G[2] += 1
print(G)

MEdu = np.array()

for x in f:
    if x[97:98] != '88' :
        MEdu.append(x[97:98])
print(MEdu)
plt.hist(MEdu)
