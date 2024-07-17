import numpy as np
import copy
from algebra_lineal import matriz_traspuesta as traspuesta, print_matriz_con_fraccciones as print_m
from munkres import *
def restar_filas(matriz):
    "Retorna una matriz en la que el minimo de cada una de sus filas se le resta a cada fila"
    matriz_restada = copy.deepcopy(matriz)
    for fila in matriz_restada:
        m = min(fila)
        for i in range(len(fila)):
            fila[i] -= m
    return matriz_restada

def restar_columnas(matriz):
    "Resta a cada fila de la matriz, el minimo de cada una de sus columna"
    matriz_restada = traspuesta(copy.deepcopy(matriz))
    for columna in matriz_restada:
        m = min(columna)
        for j in range(len(columna)):
            columna[j] -= m
    return traspuesta(matriz_restada)

def fila_con_mas_ceros(matriz: list):
    "Retorna el indice de la fila de la matriz con mas ceros"
    cant_max_ceros = 1
    indice = 0
    for i in range(len(matriz)):
        cant_ceros_fila = matriz[i].count(0)
        if cant_ceros_fila > cant_max_ceros:
            cant_max_ceros = cant_ceros_fila
            indice = i
    return indice

def columna_con_mas_ceros(matriz: list):
    "Retorna el indice de la columna de la matriz con mas ceros"
    matriz_traspuesta = traspuesta(copy.deepcopy(matriz))
    cant_max_ceros = 1
    indice = 0
    for j in range(len(matriz_traspuesta)):
        cant_ceros_columna = matriz_traspuesta[j].count(0)
        if cant_ceros_columna > cant_max_ceros:
            cant_max_ceros = cant_ceros_columna
            indice = j
    return indice

def marcar_fila(matriz: list, i: int):
    "Retorna la matriz resultante de marcar la fila con el indice dado. Cada elemento de la fila lo coloca entre <>"
    matriz0 = copy.deepcopy(matriz)
    for j in range(len(matriz0[i])):
        matriz0[i][j] = f"<{matriz0[i][j]}>"
    return matriz0

def marcar_columna(matriz: list, j: int):
    "Retorna la matriz resultante de marcar la columna con el indice dado. Cada elemento de la columna lo coloca entre <>"
    matriz0 = copy.deepcopy(matriz)
    for fila in matriz0:
        fila[j] = f"<{fila[j]}>"
    return matriz0

def marcar_linea(matriz: list):
    "Retorna la matriz resultante de marcar la linea con mas ceros. Cada elemento de la linea lo coloca entre <>"
    "Si una fila tiene la misma cantidad de ceros que una columna, se prioriza el marcado de la fila"
    i = fila_con_mas_ceros(matriz)
    j = columna_con_mas_ceros(matriz)
    if traspuesta(matriz)[j].count(0) > matriz[i].count(0):
        return marcar_columna(matriz, j)
    else:
        return marcar_fila(matriz, i)

def ceros_de_cada_linea(matriz: list):
    """Retorna una tupla de dos diccionarios
    En el primer diccionario, las claves son los indices de las filas y los valores son la cantidad de ceros de esas filas
    En el segundo diccionario, las claves son los indices de las columnas y los valores son la cantidad de ceros de esas columnas"""
    filas = {}
    columnas = {}
    tupla = (filas, columnas)
    matriz0 = copy.deepcopy(matriz)
    matriz_traspuesta = traspuesta(matriz)
    for i in range(len(matriz0)):
        filas[i] = matriz0[i].count(0)
    for j in range(len(matriz_traspuesta)):
        columnas[j] = matriz_traspuesta[j].count(0)
    return tupla

def lineas_con_mas_ceros(matriz: list):
    tupla = ceros_de_cada_linea(matriz)
    filas: dict = tupla[0]
    columnas: dict = tupla[1]
    tupla_mas_ceros = (filas, columnas)
    while len(filas) + len(columnas) > len(matriz):
        if min(filas.values()) < min(columnas.values()):
            for clave in filas.keys():
                if filas[clave] == min(filas.values()):
                    filas.pop(clave)
                    break
        else:
            for clave in columnas.keys():
                if columnas[clave] == min(columnas.values()):
                    columnas.pop(clave)
                    break
    return tupla_mas_ceros

def hay_cero(matriz: list):
    "Retorna True si hay al menos un 0 en la matriz, de lo contrario retorna False"
    for fila in matriz:
        for j in fila:
            if j == 0:
                return True
    return False

def marcar_lineas(matriz: list):
    "Retorna la matriz resultante de marcar las lineas que tienen al menos un 0, usando la menor cantidad de marcas posibles"
    "Se marca cada elemento de la linea colocandolo entre <>"
    matriz0 = copy.deepcopy(matriz)
    while hay_cero(matriz0):
        matriz0 = marcar_linea(matriz0)
    return matriz0

def cantidad_marcas(matriz: list):
    "Retorna la cantidad de lineas que se tuvieron que marcar para cubrir todos los ceros"
    matriz0 = copy.deepcopy(matriz)
    cantidad = 0
    while hay_cero(matriz0):
        matriz0 = marcar_linea(matriz0)
        cantidad += 1
    return cantidad

def min0(lista: list):
    "Retorna el elemento mas pequeño de la lista dada"
    valor_minimo = 999999999
    for elemento in lista:
        if type(elemento) == int and elemento < valor_minimo:
            valor_minimo = elemento
    return valor_minimo

def minimo(matriz: list):
    "Retorna el elemento mas pequeño de la matriz dada"
    valor_minimo = 999999999
    for fila in matriz:
        if type(min0(fila)) == int and min0(fila) < valor_minimo:
            valor_minimo = min0(fila)
    return valor_minimo

def restar_minimo_matriz(matriz: list):
    "Retorna la matriz resultante de restarle su valor minimo. Las lineas marcadas se ignoran"
    matriz0 = copy.deepcopy(matriz)
    m = minimo(matriz)
    for fila in matriz0:
        for j in range(len(fila)):
            if type(fila[j]) == int:
                fila[j] -= m
    return matriz0

def hungaro(matriz: list):
    matriz0 = copy.deepcopy(matriz)
    print_m(matriz0); print()
    matriz0 = restar_filas(matriz0)
    print_m(matriz0); print()
    matriz0 = restar_columnas(matriz0)
    print_m(matriz0); print()
    cant_marcas = cantidad_marcas(matriz0)
    matriz0 = marcar_lineas(matriz0)
    print_m(matriz0); print()
    if cant_marcas < len(matriz0): # El algoritmo continua
        matriz0 = restar_minimo_matriz(matriz0)
        print_m(matriz0); print()



def hungaro_munkres(matriz_costo):
    m = Munkres()

    asignaciones = m.compute(matriz_costo)
    
    asignacionesOptimas = []
    total = 0
    for row, column in asignaciones:
        valor = matriz_costo[row][column]
        asignacionesOptimas.append((row, column))
        total += valor      
    return asignacionesOptimas, total

filas = int(input(" Introduzca el numero de filas: \n> "))
col = int(input(" Introduzca el numero de columnas: \n> "))

matriz = []

for i in range(filas):
    array = []

    for j in range(col):
        array.append(int(input(f'Diga el valor de ({i},{j}): \n> ')))

    matriz.append(array)

print(matriz, '\n')

hungaro(matriz)
asig, total = hungaro_munkres(matriz)
print(asig)
print(total)

