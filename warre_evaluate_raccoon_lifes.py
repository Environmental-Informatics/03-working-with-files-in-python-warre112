
"""
Created on Fri Jan 31 14:05:46 2020

@author: warre112
"""
"""
Assignment 04- Raccoon Life
Les Warren
Created Friday, January 31, 2020

This program is designed to assess the life of George, the raccoon. Functions
included: creating lists, using a dictionary, summary statistics, and
 saving to .txt file
"""

"""Input File"""

george = open( "2008Male00006.txt", "r" )
##opens file. "r= read"
print(george)

first= george.readline()
#specifys to read only first line
lines= george.readlines()
#reads next remaining lines (not including the first)
last= lines[14]
#specifys the last line of data

print(lines)
george.close()
#closes read file 

Data = [0]*len(lines) #makes a list with values of "0"
for lidx in range(len(lines)-1):
        Data[lidx] = lines[lidx].split(",") #values split by commas
        Data[lidx][3] = int(Data[lidx][3]) #changing to integers
        Data[lidx][4:6] = map(float,Data[lidx][4:6]) #changing to float
        Data[lidx][8:15] = map(float,Data[lidx][8:15]) #chaning to float
# assigning correct type to each value. Starts with row "0" (N-1)
print(Data)

first= first.split(",") 


"""Dictionary"""

raccoon= dict() #creating blank dictionary
Data2 = [0]* 15 #blank list of 15 
for i in range(15):
    Data2[i] = [] #15 blank lists
for i in range(15):
    for j in range(14):
        Data2[i].append(Data [j][i]) #loop to take first column of 14 rows
for j in range(15):
        raccoon[first[j]]= Data2[j]
raccoon #view of data
Data2 

"""Summary Statistics"""

from math import sqrt

def listmean(lst):
    return sum(lst)/len(lst)
#function to calculate mean of list
    
listmean(raccoon["Energy Level"]) #test

def listsum(lst):
    return sum(lst)
#function to calculate sum of list
    
listsum(raccoon["Energy Level"]) #test


def distance(x1, x2, y1, y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)
#fucntion to calculate distance traveled between x,y of each step

distance(5,15,5,15) #test

Movement= [0]*14 #list of values of 0
for i in range(1,14):
    Movement[i]=distance(raccoon[' X'][i-1], raccoon[' X'][i], raccoon[' Y'][i-1], raccoon[' Y'][i])
    #computes distance 
Movement 
raccoon['Movement']= Movement #adds to dictionary

listmean(raccoon["Energy Level"]) #calculating mean Energy Level 

def averxy():
    return listmean(raccoon[' X']), listmean(raccoon[' Y'])
#function to calculate average X and Y value
averxy() #tesing function 

listsum(raccoon['Movement']) #calculating sum of Movement 
#=

"""Creating new .txt file"""

file= open("Warre112_Georges_life.txt","w")
#opens new .txt file with ability to write 

file.write("Raccoon name: George \n") 
file.write("Average location: 591189.034454322, 4504604.085012094 \n")
file.write("Distance traveled: 593.9382753487247 \n")
file.write("Average energy level: 563.6214285714285 \n")
file.write("Raccoon end state: George number 6 died from starvation \n")
#file.write allows to write to file.
#"\n" specifies the end of the line

file.write("\n") #blank line
file.write("Date"+"\t"+"Time"+"\t"+"X"+"\t"+"Y"+"\t"+"Alseep"+"\t"+"Behavior"+"\t"+"Distance"+"\n")
##Wrties header information. "\t" specifies to tab between header names
for d in range(14):
    file.write(str(raccoon['Day'][d])+"\t"+str(raccoon['Time'][d])+"\t"+str(raccoon[' X'][d])+"\t"+str(raccoon[' Y'][d])+"\t"+str(raccoon[' Asleep'][d])+"\t"+str(raccoon['Behavior Mode'][d])+"\t"+str(raccoon['Movement'][d])+"\n")
#loop function to write the specified lines of data
file.close()    
#closes file
