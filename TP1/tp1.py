import copy
import math
import numpy as np
import matplotlib.pyplot as plt

ROJO = '\033[91m'
RESET = '\033[0m'
TEMPERATURA_ARRIBA = 10
TEMPERATURA_ABAJO = 11
TEMPERATURA_IZQUIERDA = 12
TEMPERATURA_DERECHA = 13
LARGO_PLANCHA = 5
ANCHO_PLANCHA = 4
DISCRETIZACION = 1

def multiplicar_vector_constante(vector, constante, dimension):
    for i in range(dimension):
        vector[i] = round(vector[i] * constante,2)
    return vector
def restar_vectores (vector_minuendo, vector_sustraendo, dimension):
    vector_resultado = []
    for i in range(dimension):
        resultado = round(vector_minuendo[i] - vector_sustraendo[i],2)
        vector_resultado.append(resultado)
    return vector_resultado
def calcular_dimencion(longitud, discretizacion):
    return (int ((longitud / discretizacion) + 1))

def crear_placa_inicial (largo, ancho):
    placa = []
    for i in range(largo):
        fila_placa = []
        for j in range(ancho):
            if (i == 0):
                if (j == 0 or j == ancho - 1):
                    fila_placa.append(0)
                else:
                    fila_placa.append(TEMPERATURA_ARRIBA)
            elif (i == (largo - 1)):
                if (j == 0 or j == ancho - 1):
                    fila_placa.append(0)
                else:
                    fila_placa.append(TEMPERATURA_ABAJO)
            elif (j == 0):
                fila_placa.append(TEMPERATURA_IZQUIERDA)
            elif (j == (ancho - 1)):
                fila_placa.append(TEMPERATURA_DERECHA)
            else:
                fila_placa.append(0)
        placa.append(fila_placa)
    return placa

def crear_matriz_de_ceros (largo, ancho):
    contador = 0
    cantidad_nodos = largo * ancho
    matriz = []
    for i in range(cantidad_nodos):
        fila_matriz = []
        for j in range(cantidad_nodos):
            fila_matriz.append(0)
            contador = contador + 1
        matriz.append(fila_matriz)
    return matriz

def no_es_borde_placha(posicion, dimension, largo_plancha, ancho_plancha):
    if (posicion < largo_plancha):
        return False

    busqueda = largo_plancha - 1
    while (busqueda < dimension - largo_plancha):
        if (posicion == busqueda or posicion == busqueda + 1):
            return False
        busqueda += largo_plancha

    if (posicion < dimension and posicion > dimension - largo_plancha):
        return False
    return True

def crear_matriz_A (largo, ancho):
    matriz = crear_matriz_de_ceros(largo, ancho)
    dimension = largo * ancho
    for i in range(dimension):
        if (no_es_borde_placha(i, dimension, largo, ancho)):
            matriz[i][i] = 4
            matriz[i][i - largo] = -1
            matriz[i][i + largo] = -1
            matriz[i][i + 1] = -1
            matriz[i][i - 1] = -1
        else :
            matriz[i][i] = 1
    return matriz


def imprimir_matriz (matriz):
    f=0
    for fila in matriz:
        f+=1
        c=0
        for elemento in fila:
            c+=1
            if (c ==f): print (ROJO+ str(elemento)+ RESET, end=" " )
            else: print (elemento, end=" ")
        print("\n")

def imprimir_vector (vector):
    for elemento in vector:
        print(round(float(elemento),2), end=" ")
    print("\n")

def aplicar_eliminacion_gauseana (matriz, dimension):
    for i in range(dimension):
        vector_sustraendo = copy.deepcopy(matriz[i])
        elemento_diagonal = matriz[i][i]

        print(f"FILA : {i}")
        if (elemento_diagonal != 0):
            for j in range(i+1, dimension):
                elemento_eliminar = matriz[j][i]

                if (elemento_eliminar != 0):
                    print(f"elemento eliminar : {elemento_eliminar}, fila: {j} columna: {i}")

                    multiplicador = round(elemento_eliminar/elemento_diagonal,2)
                    if (multiplicador != 0 ):
                        print(f"multiplicador : Eliminar {elemento_eliminar} * Diagonal {elemento_diagonal} = {multiplicador}")
                        vector_sustraendo = multiplicar_vector_constante(vector_sustraendo, multiplicador, dimension)
                        print(f"vector sustraendo ")
                        imprimir_vector(vector_sustraendo)
                        imprimir_vector(matriz[j])
                        matriz[j] = restar_vectores(matriz[j], vector_sustraendo, dimension)
                        imprimir_vector(matriz[j])
    return matriz



def main ():
    largo_placa_uno = calcular_dimencion(LARGO_PLANCHA, DISCRETIZACION)
    ancho_placa_uno = calcular_dimencion(ANCHO_PLANCHA, DISCRETIZACION)
    placa_uno = crear_placa_inicial(largo_placa_uno, ancho_placa_uno)
    imprimir_matriz(placa_uno)
    A = crear_matriz_A(largo_placa_uno,ancho_placa_uno)
    imprimir_matriz(A)
    B = aplicar_eliminacion_gauseana(copy.deepcopy(A), largo_placa_uno * ancho_placa_uno)
    print("pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
    imprimir_matriz(B)

    return 0

main ()