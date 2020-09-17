# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:57:15 2020

@author: User
"""

from tkinter import *
raiz=Tk()
raiz.title('Volumen de un Cilindro')

import math

altura = float (input ('Ingrese el valor de altura: '))
radio = float (input ('Ingrese el valor de radio: '))
volumen=math.pi*radio**2*altura
area=math.pi**2*radio*(radio+altura)
print ('Valor de area: ' + repr (area))
print ('Valor de volumen: ' + repr (volumen))
raiz.mainloop()
