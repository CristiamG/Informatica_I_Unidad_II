# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:55:50 2020

@author: User
"""

import math

a = float (input ('Ingrese el valor de a: '))
b = float (input ('Ingrese el valor de b: '))
c = float (input ('Ingrese el valor de c: '))
discriminante=b*b-4.0*a*c
if discriminante<0:
    discriminante=-discriminante
    print ('Soluciones imaginarias')
else:
    print ('Soluciones reales')
if a!=0:
    x1=(-b+math.sqrt(discriminante))/2.0*a
    x2=(-b-math.sqrt(discriminante))/2.0*a
else:
    x1=0
    x2=0
    print ('No es una ecuacion cuadratica')
print ('Valor de discriminante: ' + repr (discriminante))
print ('Valor de x1: ' + repr (x1))
print ('Valor de x2: ' + repr (x2))
