# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 12:24:08 2023

@author: xahil
"""

# space_guion = [-1,-1]
name = 'juli0 lopez-gavilán'
temp_name = name
if temp_name.isalpha():
    print('solo letras (un nombre, una palabra): true')
else:
    simbolos_a_quitar = (' ','-')
    for simbolo in simbolos_a_quitar:
            temp_name = temp_name.replace(simbolo, "")
    if temp_name.isalpha():
        print('True')
        print('solo letras (un nombre, una palabra): true')
    else:
        print('False')
        print('caracter diferente a guion o espacio')



    # print('caracter diferente a letra alfabetica')
    # if not name.find(" ") == -1:
    #     space_guion[0] = 1 # un caracter es '
        
        
        
        
        
    #     name.remove()
    # else:
    #     space_guion[0] = 0
    # if not name.find("-") == -1:
    #     space_guion[1] = 1 # un caracter es '-'
    # else:
    #     space_guion[1] = 0
        
# space = name.find(" ")
# print(space)
