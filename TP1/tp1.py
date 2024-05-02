import copy
import math
import numpy as np
import matplotlib.pyplot as plt

ROJO = '\033[91m'
RESET = '\033[0m'
TEMPERATURA_ARRIBA = 63
TEMPERATURA_ABAJO = 44
TEMPERATURA_IZQUIERDA = 26
TEMPERATURA_DERECHA = 72
LARGO_PLANCHA = 5
ANCHO_PLANCHA = 4
DISCRETIZACION = 0.5


def imprimir_plancha (vector, ancho, largo):
    for i in range(ancho):
        for j in range (largo):

            print("{:.0f}".format(vector[ j + i * largo]), end=" ")
        print("\n")
def imprimir_matriz (matriz):
    f=0
    for fila in matriz:
        f+=1
        c=0
        for elemento in fila:
            c+=1
            if (c == f): print (ROJO+ str(elemento)+ RESET, end=" " )
            else: print (elemento, end=" ")
        print("\n")

def imprimir_vector (vector):
    for elemento in vector:
        print("{:.2f}".format(elemento), end=" ")
    print("\n")

def multiplicar_vector_constante(vector, constante, dimension):
    for i in range(dimension):
        vector[i] = vector[i] * constante
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
    for i in range(ancho):
        fila_placa = []
        for j in range(largo):
            if (i == 0):
                if (j == 0 or j == largo - 1):
                    fila_placa.append(1)
                else:
                    fila_placa.append(TEMPERATURA_ARRIBA)
            elif (i == (ancho - 1 )):
                if (j == 0 or j == largo - 1):
                    fila_placa.append(1)
                else:
                    fila_placa.append(TEMPERATURA_ABAJO)
            elif (j == 0):
                fila_placa.append(TEMPERATURA_IZQUIERDA)
            elif (j == (largo - 1)):
                fila_placa.append(TEMPERATURA_DERECHA)
            else:
                fila_placa.append(0)
        placa.append(fila_placa)
    return placa

def crear_matriz_de_ceros (largo, ancho):
    cantidad_nodos = largo * ancho
    matriz = []
    for i in range(cantidad_nodos):
        fila_matriz = []
        for j in range(cantidad_nodos):
            fila_matriz.append(0)
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

def crear_vector_b (largo, ancho):
    vector = []
    for i in range(ancho):
        for j in range(largo):
            if (i == 0):
                if (j == 0 or j == largo - 1):
                    vector.append(1)
                else:
                    vector.append(TEMPERATURA_ARRIBA)
            elif (i == (ancho - 1)):
                if (j == 0 or j == largo - 1):
                    vector.append(1)
                else:
                    vector.append(TEMPERATURA_ABAJO)
            elif (j == 0):
                vector.append(TEMPERATURA_IZQUIERDA)
            elif (j == (largo - 1)):
                vector.append(TEMPERATURA_DERECHA)
            else:
                vector.append(0)
    return vector


'''................................................................................'''

def aplicar_eliminacion_gauseana (matriz, dimension, vector):
    A = np.array(matriz)
    b = np.array(vector)
    Ab = np.hstack((A, b.reshape(-1, 1)))
    for i in range(dimension):
        for j in range(i + 1, dimension):
            c = Ab[j][i] / Ab[i][i]
            for k in range(i, dimension+1):
                Ab[j][k] -= c * Ab[i][k]
    return Ab

def sustitucion_inversa(matrix, vector, dimension):
    x = np.zeros(dimension)
    for i in range(dimension - 1, -1, -1):
        b = vector[i]
        variable = np.dot(matrix[i, i+1:], x[i+1:])
        elemento = matrix[i, i]
        x[i] = (b - variable) / elemento
    return x

def resolucion_por_gauss (largo, ancho):
    dimension = largo * ancho
    A = crear_matriz_A(largo, ancho)
    b = crear_vector_b(largo, ancho)
    Ab = aplicar_eliminacion_gauseana(A, dimension, b)
    A_con_eliminacion = Ab[:, :dimension]
    b_con_eliminacion = Ab[:, dimension]
    resultado = sustitucion_inversa(A_con_eliminacion, b_con_eliminacion, dimension)
    return resultado

'''.....................................................................................'''
def crear_solucion_inicial (dimension, elemento):
    vector = []
    for i in range (dimension):
        vector.append(elemento)
    return vector

def aplicar_metodo_jacobi (matriz, vector, solucion_inicial, tolerancia, max_iteraciones, dimension):

       x_acutal = np.copy(solucion_inicial)
       x_siguiente = np.zeros_like(x_acutal)
       A = np.array(matriz)
       b = np.array(vector)
       for j in range(max_iteraciones):
           for i in range(dimension):
               suma_ax = np.dot(A[i, :i], x_acutal[:i]) + np.dot(A[i, i + 1:], x_acutal[i + 1:])
               x_siguiente[i] = (b[i] - suma_ax) / A[i, i]


           if (np.sqrt(np.sum((x_siguiente - x_acutal) ** 2) / np.sqrt(np.sum(x_siguiente) ** 2)) < tolerancia):
               return x_siguiente
           x_acutal = np.copy(x_siguiente)
       return 0
def resolucion_por_jacobi (largo, ancho):
    dimension = largo * ancho
    A = crear_matriz_A(largo, ancho)
    b = crear_vector_b(largo, ancho)
    x0 = crear_solucion_inicial (dimension, 0)
    tolerancia = 0.0000001
    tolerancia_iteraciones = 100000000
    x = aplicar_metodo_jacobi(A, b, x0, tolerancia, tolerancia_iteraciones, dimension)
    return x

'''.....................................................................................'''

def aplicar_metodo_gauss_seidez(matriz, vector, solucion_inicial, tolerancia, max_iteraciones, dimension):
    x_actual = np.copy(solucion_inicial)
    x_siguiente = np.zeros_like(x_actual)
    A = np.array(matriz)
    b = np.array(vector)
    for i in range (max_iteraciones):
        for i in range (dimension):
            x_siguiente[i] = (b[i] - np.dot(A[i, :i], x_siguiente[:i]) - np.dot(A[i, i + 1:], x_actual[i + 1:])) / A[i, i]

        if (np.sqrt(np.sum((x_siguiente - x_actual) ** 2) / np.sqrt(np.sum(x_siguiente) ** 2)) < tolerancia):
            return x_siguiente

        x_actual = np.copy(x_siguiente)
    return 0

def resolucion_por_gauss_seidez(largo, ancho):
    dimension = largo * ancho
    A = crear_matriz_A(largo, ancho)
    imprimir_matriz(A)

    b = crear_vector_b(largo, ancho)
    imprimir_vector(b)

    x0 = crear_solucion_inicial(dimension, 0)
    tolerancia = 0.000001
    tolerancia_iteraciones = 100000000
    x = aplicar_metodo_gauss_seidez(A, b, x0, tolerancia, tolerancia_iteraciones, dimension)
    return x

def main ():
    largo_placa_uno = calcular_dimencion(LARGO_PLANCHA, DISCRETIZACION)
    ancho_placa_uno = calcular_dimencion(ANCHO_PLANCHA, DISCRETIZACION)
    placa_uno = crear_placa_inicial(largo_placa_uno, ancho_placa_uno)
    x = resolucion_por_gauss(largo_placa_uno, ancho_placa_uno)
    y = resolucion_por_jacobi(largo_placa_uno, ancho_placa_uno)
    z = resolucion_por_gauss_seidez(largo_placa_uno, ancho_placa_uno)
    imprimir_vector(x)
    imprimir_vector(y)
    imprimir_vector(z)
    imprimir_matriz(placa_uno)
    imprimir_plancha(y,ancho_placa_uno, largo_placa_uno)
    plt.figure()
    plt.quiver(x, y, scale=5)
    plt.show()
    return 0

main ()