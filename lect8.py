# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:07:59 2020

@author: Tim
"""

# =============================================================================
# #Class
# class FirstClass:
#     #Attribute
#     variable = "blah"
#     #Function
#     def function(self):
#         print("This message inside the class")
# #Object        
# myobjectx = FirstClass()
# print(myobjectx.variable)
# =============================================================================


class MyClass:
    def multiplyNumbers(self,num1,num2):
        total = 0
        for i in range(num2):
            total = total + num1
        return total


class MyClass:
    #Self makes function belong to class
    def multiplyNumbers(self,num1,num2):
        total = 0
        if num1 < 100 and num2 < 100:
            for i in range(num2):
                total = total + num1    
            return total
        else:
            print("-1")
            
num1 = int(input()) 
num2 = int(input())
#Initialisation 
myObject = MyClass()
#Calls object with function 
myObject.multiplyNumbers(num1,num2)