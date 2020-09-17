# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 01:35:19 2020

@author: User
"""

contrasena="informatica"

for i in range(3):
    entrada=input("Indica la contraseña para acceder: ")
    if entrada==contrasena:

        print("Bienvenido al Curso de 'Informática I'")
        break
    elif i==2:
        print("Superaste el máximo de intentos.")
