# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 11:12:27 2023

@author: xahil
"""


#   FUNCTIONS
def check_name(name):
    temporal_name = name
    char_to_remove = (' ','-')
    for char in char_to_remove:
            temporal_name = temporal_name.replace(char, "")
    
    if temporal_name.isalpha():
        return True
    else:
        return False

def check_age(age):        
    if age.isdigit() == True:
        if int(age) > 4 and int(age) <=100:        
            return True
        else:
            return False
    else:        
        return False
    
def check_height(height):
    if height.isalpha() == True:
        return False
    else:
        digit = 0
        separator = 0
        for q in range(len(height)):
            if height[q].isdigit() == True:
                digit+=1
            else:
                separator +=1
        if not separator == 1:
            return False
        else:
            if int(height[0]) == 0:
                if not int(height[2]) > 3:
                    return False
            elif int(height[0]) == 1:
                return True
            elif int(height[0]) == 2:
                if int(height[2]) > 5:
                    return False
                else:
                    return True
            else:
                print('This height value is not admissible')
                return False
        
        
#   MAIN            
path = './Exercise 1-Hello World.txt'
with open(path,"r") as exercise_order:
    print(exercise_order.read())

check = False
while check == False:
    name = input('What is your name?: ')    
    if check_name(name) == True:
        check = True
    else:
        print('You must enter a valid name')
    
check = False
while check == False:
    age = input('How old are you?: ') 
    if check_age(age) == True:
        check = True
    else:
        print('You must enter a valid age value')

check = False
while check == False:
    height = input('What is your height in meters? Example 1.65: ')
    if check_height(height) == True:
        check = True
    else:
        print('You must enter a valid height value')
        
print(f'The user {name}, {age} years old, is {height} meters tall.”')

