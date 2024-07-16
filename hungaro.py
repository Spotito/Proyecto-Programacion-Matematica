import numpy as np
import copy
from algebra_lineal import matriz_traspuesta as traspuesta, print_matriz_con_fraccciones as print_m

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

def eliminar_fila(matriz: list, i: int):
    "Retorna la matriz resultante de eliminar la fila dada"
    matriz0 = copy.deepcopy(matriz)
    matriz0.pop(i)
    return matriz0

def eliminar_columna(matriz: list, j: int):
    "Retorna la matriz resultante de eliminar la columna dada"
    matriz0 = copy.deepcopy(matriz)
    for i in range(len(matriz0)):
        matriz0[i].pop(j)
    return matriz0

def eliminar_linea(matriz: list):
    "Retorna la matriz resultante de eliminar la linea con mas ceros"
    i = fila_con_mas_ceros(matriz)
    j = columna_con_mas_ceros(matriz)
    if traspuesta(matriz)[j].count(0) > matriz[i].count(0):
        return eliminar_columna(matriz, j)
    else:
        return eliminar_fila(matriz, i)

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

def eliminar_lineas(matriz: list):
    "Retorna la matriz resultante de eliminar las lineas con ceros, usando la menor cantidad de eliminaciones"
    matriz0 = copy.deepcopy(matriz)
    while hay_cero(matriz0):
        matriz0 = eliminar_linea(matriz0)
    return matriz0

def minimo(matriz: list):
    "Retorna el elemento mas pequeño de la matriz dada"
    valor_minimo = matriz[0][0]
    for fila in matriz:
        if min(fila) < valor_minimo:
            valor_minimo = min(fila)
    return valor_minimo

def restar_minimo_matriz(matriz: list):
    "Retorna la matriz resultante de restarle su valor minimo"
    matriz0 = copy.deepcopy(matriz)
    m = minimo(matriz)
    for fila in matriz0:
        for j in range(len(fila)):
            fila[j] -= m
    return matriz0


matriz=[[11800, 15000, 20000, 0],
        [12500, 13000, 14400, 0],
        [20000, 18000, 23000, 0],
        [18000, 17000, 16000, 0]]

print_m(matriz)
print(ceros_de_cada_linea(matriz))
print(lineas_con_mas_ceros(matriz)); print()
matriz = restar_filas(matriz)
print_m(matriz)
print(ceros_de_cada_linea(matriz))
print(lineas_con_mas_ceros(matriz)); print()
matriz = restar_columnas(matriz)
print_m(matriz)
print(ceros_de_cada_linea(matriz))
print(lineas_con_mas_ceros(matriz)); print()
matriz = eliminar_lineas(matriz)
print_m(matriz)
print(ceros_de_cada_linea(matriz))
print(lineas_con_mas_ceros(matriz)); print()
matriz = restar_minimo_matriz(matriz)
print_m(matriz)
print(ceros_de_cada_linea(matriz))
print(lineas_con_mas_ceros(matriz)); print()