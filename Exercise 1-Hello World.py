# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 11:12:27 2023

@author: xahil
"""


#   FUNCTIONS
def check_name(name):
    if name.isalpha():
        return True
    else:
        return False

def check_age(age):        
    if age.isdigit() == True:
        # print('solo digitos')
        if int(age) > 4 and int(age) <=100:        
            return True
        else:
            # print('edad fuera de rango permitido')
            return False
    else:
        # print('algo mas que difitos')        
        return False
    
def check_height(height):
    # means, enter value was a letter
    if height.isalpha() == True:
        # hubo una letra
        return False
    else:
        # no hay letra
        digit = 0
        separator = 0
        for q in range(len(height)):
            if height[q].isdigit() == True:
                digit+=1
            else:
                separator +=1
        if not separator == 1:
            # no es letra, pero mas de un separador'
            return False
        else:
            print('supuestamente, numero decimal bueno')
            if int(height[0]) == 0:
                if not int(height[2]) > 3:
                    print('altura mas pequeña que la del bebe mas pequeño del mundo' )
                    return False
            # persona que mide 1 metro con algo
            elif int(height[0]) == 1:
                # print('altura buena')
                return True
            #persona que mide 2 metros con algo
            elif int(height[0]) == 2:
                if int(height[2]) > 5:
                    print('altura mas alta que la persona mas alta del mundo')
                    return False
                else:
                    print('persona de mas de 2 metros y altura aceptable')
                    return True
            else:
                print('altura imposible')
                return False
            # return True
        
        
#   MAIN            
path = 'D:/00-mis programas/30 ejercicios/Exercise 1-Hello World/Exercise 1-Hello World.txt'
with open(path,"r") as exercise_order:
    print(exercise_order.read())

check = False
while check == False:
    name = input('what is your name?: ')    
    if check_name(name) == True:
        check = True
    else:
        print('you must enter a name that contains only letters')
    
check = False
while check == False:
    age = input('how old are you?: ') 
    if check_age(age) == True:
        check = True
    else:
        print('you must enter a valid age value')

check = False
while check == False:
    height = input('what is your height in meters[a.b]?: ')
    if check_height(height) == True:
        check = True
    else:
        print('you must enter a valid height value')
        
print(f'The user {name}, {age} years old, is {height} meters tall.”')

