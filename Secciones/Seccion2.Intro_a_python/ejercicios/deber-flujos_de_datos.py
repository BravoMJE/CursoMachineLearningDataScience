# -*- coding: utf-8 -*-

"""
******************************************************************************

EJERCICIOS

******************************************************************************
"""

# Dado el diccionario:
dias_semana = {"lunes":1,
               "martes":2,
               "miercoles": 3,
               "jueves": 4,
               "viernes": 5, 
               "sabado": 6,
               "domingo": 7
               }

#%%
"""
De dicho diccionario, convertir todas las claves a mayúsculas, usando un bucle
"""
dias_semana_mayuscula ={}
for dia, valor in dias_semana.items():
    dias_semana_mayuscula[dia.upper()] = valor
    
dias_semana = dias_semana_mayuscula
print(dias_semana)

#%%    
"""
 De dicho diccionario, crear una lista de los dias de la semana que contengan 
 la letra "O"
"""
dias_con_O = []

for dia in dias_semana:
    if "O" in dia:
        dias_con_O.append(dia)

print(dias_con_O)