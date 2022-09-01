"""

@author: Nadine
Task#1
"""
import statistics
import sys

x = eval(input()) #takes the input list

def MyFunc(x):
    integer_li = []
    float_li = []
    
    for i in x:   # if it is neither float or integer it outputs 0
        if type(i) != int and type (i) != float :
            print(0)
            sys.exit()
         
        
    for flag in x: #divides the list to integers and floats then print the mean and the max no. respectively
        if type(flag) == int:
            integer_li.append(flag)
        if type (flag) == float:
            float_li.append(flag) 
        
                
    print("  Mean value of integers is : ",statistics.mean(integer_li), ", Max number of floats is : ", max(float_li) )

   
  
# Driver Code

MyFunc(x)