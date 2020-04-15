# -*- coding: utf-8 -*-

#%%
"""
******************************************************************************

EJERCICIOS

******************************************************************************
"""

#%%
"""
 Crear un diccionario cuyas claves sean los tres primeros dias de la semana y los 
 valores sean la posicion en la semana de dicho dia
"""

diccionarioDias = {
    "Lunes": 1,
    "Martes": 2,
    "Miercoles": 3
    }

#%%
"""
 De dicho diccionario, convertir todas las claves a mayúsculas
"""

diccionarioDias["LUNES"] = diccionarioDias.pop("Lunes")
diccionarioDias["MARTES"] = diccionarioDias.pop("Martes")
diccionarioDias["MIERCOLES"] = diccionarioDias.pop("Miercoles")

print(diccionarioDias)