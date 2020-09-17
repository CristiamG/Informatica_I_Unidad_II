# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:04:40 2020

@author: User
"""

suma=0
sera_factor=1

sera_perfecto=int(input('ingrese un numero: '))

while sera_factor < sera_perfecto :
    if (sera_perfecto%sera_factor==0):
        suma=suma+sera_factor
    sera_factor=sera_factor+1
if suma==sera_perfecto:
    print("===",sera_perfecto,"===  Si es perfecto  ===")
else:
    print(sera_perfecto,"No es perfecto")
