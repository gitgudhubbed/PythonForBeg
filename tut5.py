# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:21:48 2020

@author: Tim
"""
#LISTS
numberList = [1,2,3,4,5]
stringList = ["This", "Is", "Python"]

#Function to take a list of numbers as parameters and add them up
def counter(numberList):
    total = sum (numberList)
    return total

#Function to take a list of numbers as parameters and mutiply them  
def multiply(numberList):
    total = 1
    for x in numberList:
        total = total * x
    return total
  
#Function to take a list of strings and concatenate into one String
def unify(stringList): 
    final = ""
    for x in stringList:
        final += str(x + " ") 
    return final

#Print results of functions
print(counter(numberList))
print(multiply(numberList))
print(unify(stringList))
