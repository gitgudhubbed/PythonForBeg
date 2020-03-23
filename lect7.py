# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:04:34 2020

@author: Tim
"""


#Example function for multplication without * operator, to use for unit testing

    
 
# print(multiplyNumbers(num1,num2))

import unittest

class MyClass:
    #Self makes function belong to class
    def multiplyNumbers(self,num1,num2):
        total = 0
        if type(num1) != int or type(num2) != int:
            return -1
        if num2 <=0:
            num2 = -num2
            num1 = -num1
        if num1 and num2 < 100:
            for i in range(num2):
                total = total + num1    
            return total
        else:
            return -1

class multiplyNumbersTest(unittest.TestCase):
    def setUp(self):
        self.myclass1 = MyClass()
        
    def tearDown(self):
        del self.myclass1
         
    def testTwoPostiveNumbers(self):
        self.assertEqual(self.myclass1.multiplyNumbers(8,5), 40)
        
    def testTwoInvalidLargePostiveNumbers(self):
        self.assertEqual(self.myclass1.multiplyNumbers(102,989), -1)
        
    def testTwoNegativeNumbers(self):
        self.assertEqual(self.myclass1.multiplyNumbers(-1, -99), 99)
        
    def testOneNegativeOnePositiveNumber(self):
        self.assertEqual(self.myclass1.multiplyNumbers(-8, 34), -272)
        
    def testTwoZeroNumbers(self):
        self.assertEqual(self.myclass1.multiplyNumbers(0, 0), 0)
        
    def testTwoCharacters(self):
        self.assertEqual(self.myclass1.multiplyNumbers('a', 'b'), -1)
        
            
if __name__=='__main__':
    unittest.main()

            
#num1 = int(input()) 
#num2 = int(input())
#Initialisation 
#myObject = MyClass()
#Calls object with function 
#myObject.multiplyNumbers(num1,num2)
    
        