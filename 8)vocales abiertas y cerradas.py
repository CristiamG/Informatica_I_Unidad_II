# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 01:42:02 2020

@author: User
"""


#Variable de entrada - Se ingresa y almacena la frase
frase=str(input("Ingrese la frase en la que desea reemplazar las vocales por signos: "))

#Variable auxiliar 1 - Define la variable frase1 - Reemplaza en frase la vocal a por el signo +
frase1=frase.replace("a","+")

#Variable auxiliar 2 - Define la variable frase2 - Reemplaza en frase la vocal e por el signo +
frase2=frase1.replace("e","+")

#Variable auxiliar 3 - Define la variable frase3 - Reemplaza en frase la vocal i por el signo -
frase3=frase2.replace("i","-")

#Variable auxiliar 4 - Define la variable frase4 - Reemplaza en frase la vocal o por el signo +
frase4=frase3.replace("o","+")

#Variable auxiliar 5 - Define la variable frase5 - Reemplaza en frase la vocal u por el signo -
frase5=frase4.replace("u","-")

#Variable de salida - Imprime frase5
print(frase5)
