"""
Dadas las matrices A y B, de dimensión 100x100, hallar:
a) AB
b) BA
c) A
tB, ABt
,(AB)
t
d) la suma de los elementos de la diagonal de los resultados anteriores.
e) los coeficientes máximos y mínimos de los resultados anteriores
f) la posición de los coeficientes máximos y mínimos de los resultados anteriores
"""

# Las primeras fuciones son las herramientas para resolver los problemas y luego se los resuelve con dichas herramientas
import random

DIMENSION = 100

def imprimir_matriz (matriz):
    for fila in matriz:
        for elemento in fila:
            print (elemento, end=" ")
        print("\n")

def buscar_posicion (valor, matriz):
    casillas = []
    for i in range (DIMENSION):
        for j in range (DIMENSION):
            if valor == matriz[i][j]:
                casillas.append([i+1, j+1])
    return casillas

def coeficiente_minimo(matriz):
    resultado = matriz[1][1]
    for i in range (DIMENSION):
        for j in range (DIMENSION):
            if resultado > matriz[i][j]:
                resultado = matriz[i][j]
    return resultado

def coeficiente_maximo(matriz):
    resultado = matriz[1][1]
    for i in range (DIMENSION):
        for j in range (DIMENSION):
            if resultado < matriz[i][j]:
                resultado = matriz[i][j]
    return resultado

def sumar_diagonal (matriz):
    resultado = 0
    for i in range (DIMENSION):
        resultado += matriz[i][i]
    return resultado

def transponer_matriz (matriz):
    matriz_resultado = []
    for i in range (DIMENSION):
        fila_resultado = []
        for j in range (DIMENSION):
            fila_resultado.append(matriz[j][i])
        matriz_resultado.append(fila_resultado)
    return matriz_resultado

def multiplicar_matizes (matrizA, matrizB):
    matriz_resultado = []
    for i in range(DIMENSION):
        fila_resultado = []
        for j in range(DIMENSION):
            elemento_resultado = 0
            for k in range (DIMENSION):
                elemento_resultado = elemento_resultado + matrizA[i][k] * matrizB[k][j]
            fila_resultado.append(elemento_resultado)
        matriz_resultado.append(fila_resultado)
    return matriz_resultado

#ejercicio a
def ejercicio_a (matrizA, matrizB):
    matriz_resultado = multiplicar_matizes(matrizA, matrizB)
    return matriz_resultado
#ejercicio b
def ejercicio_b (matrizA, matrizB):
    matriz_resultado = multiplicar_matizes(matrizB, matrizA)
    return matriz_resultado
#ejercicio c
def ejercicio_c_i (matrizA, matrizB):
    matriz_resultado = multiplicar_matizes(transponer_matriz(matrizA), matrizB)
    return matriz_resultado

def ejercicio_c_ii (matrizA, matrizB):
    matriz_resultado = multiplicar_matizes(matrizA, transponer_matriz(matrizB))
    return matriz_resultado

def ejercicio_c_iii (matrizA, matrizB):
    matriz_resultado = transponer_matriz((multiplicar_matizes(matrizA, matrizB)))
    return matriz_resultado
#ejercicio d
def ejercicio_d_i (matrizA, matrizB):
    resultado = sumar_diagonal(ejercicio_a(matrizA, matrizB))
    return resultado

def ejercicio_d_ii (matrizA, matrizB):
    resultado = sumar_diagonal(ejercicio_b(matrizA, matrizB))
    return resultado

def ejercicio_d_iii (matrizA, matrizB):
    resultado = sumar_diagonal(ejercicio_c_i(matrizA, matrizB))
    return resultado

def ejercicio_d_iv (matrizA, matrizB):
    resultado = sumar_diagonal(ejercicio_c_ii(matrizA, matrizB))
    return resultado

def ejercicio_d_v (matrizA, matrizB):
    resultado = sumar_diagonal(ejercicio_c_iii(matrizA, matrizB))
    return resultado
#ejercicio e
def ejercicio_e_i_max (matrizA, matrizB):
    resultado = coeficiente_maximo(ejercicio_a(matrizA, matrizB))
    return resultado
def ejercicio_e_i_min (matrizA, matrizB):
    resultado = coeficiente_minimo(ejercicio_a(matrizA, matrizB))
    return resultado
def ejercicio_e_ii_max (matrizA, matrizB):
    resultado = coeficiente_maximo(ejercicio_b(matrizA, matrizB))
    return resultado
def ejercicio_e_ii_min (matrizA, matrizB):
    resultado = coeficiente_minimo(ejercicio_b(matrizA, matrizB))
    return resultado
def ejercicio_e_iii_max (matrizA, matrizB):
    resultado = coeficiente_maximo(ejercicio_c_i(matrizA, matrizB))
    return resultado
def ejercicio_e_iii_min (matrizA, matrizB):
    resultado = coeficiente_minimo(ejercicio_c_i(matrizA, matrizB))
    return resultado
def ejercicio_e_iv_max (matrizA, matrizB):
    resultado = coeficiente_maximo(ejercicio_c_ii(matrizA, matrizB))
    return resultado
def ejercicio_e_iv_min (matrizA, matrizB):
    resultado = coeficiente_minimo(ejercicio_c_ii(matrizA, matrizB))
    return resultado
def ejercicio_e_v_max (matrizA, matrizB):
    resultado = coeficiente_maximo(ejercicio_c_iii(matrizA, matrizB))
    return resultado
def ejercicio_e_v_min (matrizA, matrizB):
    resultado = coeficiente_minimo(ejercicio_c_iii(matrizA, matrizB))
    return resultado

#ejercicio f
def ejercicio_f_i_max (matrizA, matrizB):
    resutlado = buscar_posicion(ejercicio_e_i_max(matrizA, matrizB), ejercicio_a(matrizA, matrizB))
    return resutlado
def ejercicio_f_i_min (matrizA, matrizB):
    resutlado = buscar_posicion(ejercicio_e_i_min(matrizA, matrizB), ejercicio_a(matrizA, matrizB))
    return resutlado
def ejercicio_f_ii_max (matrizA, matrizB):
    resutlado = buscar_posicion(ejercicio_e_ii_max(matrizA, matrizB), ejercicio_b(matrizA, matrizB))
    return resutlado
def ejercicio_f_ii_min (matrizA, matrizB):
    resutlado = buscar_posicion(ejercicio_e_ii_min(matrizA, matrizB), ejercicio_b(matrizA, matrizB))
    return resutlado
def ejercicio_f_iii_max (matrizA, matrizB):
    resutlado = buscar_posicion(ejercicio_e_iii_max(matrizA, matrizB), ejercicio_c_i(matrizA, matrizB))
    return resutlado
def ejercicio_f_iii_min (matrizA, matrizB):
    resutlado = buscar_posicion(ejercicio_e_iii_min(matrizA, matrizB), ejercicio_c_i(matrizA, matrizB))
    return resutlado
def ejercicio_f_iv_max (matrizA, matrizB):
    resutlado = buscar_posicion(ejercicio_e_iv_max(matrizA, matrizB), ejercicio_c_ii(matrizA, matrizB))
    return resutlado
def ejercicio_f_iv_min (matrizA, matrizB):
    resutlado = buscar_posicion(ejercicio_e_iv_min(matrizA, matrizB), ejercicio_c_ii(matrizA, matrizB))
    return resutlado
def ejercicio_f_v_max (matrizA, matrizB):
    resutlado = buscar_posicion(ejercicio_e_v_max(matrizA, matrizB), ejercicio_c_iii(matrizA, matrizB))
    return resutlado
def ejercicio_f_v_min (matrizA, matrizB):
    resutlado = buscar_posicion(ejercicio_e_v_min(matrizA, matrizB), ejercicio_c_iii(matrizA, matrizB))
    return resutlado

def main ():
    matrizA = [[random.randint(0, 9) for _ in range(DIMENSION)] for _ in range(DIMENSION)]
    matrizB = [[random.randint(0, 9) for _ in range(DIMENSION)] for _ in range(DIMENSION)]

    imprimir_matriz(ejercicio_a(matrizA, matrizB))

    imprimir_matriz(ejercicio_b(matrizA, matrizB))

    imprimir_matriz(ejercicio_c_i(matrizA, matrizB))
    imprimir_matriz(ejercicio_c_ii(matrizA, matrizB))
    imprimir_matriz(ejercicio_c_iii(matrizA, matrizB))

    print(ejercicio_d_i(matrizA, matrizB))
    print(ejercicio_d_ii(matrizA, matrizB))
    print(ejercicio_d_iii(matrizA, matrizB))
    print(ejercicio_d_iv(matrizA, matrizB))
    print(ejercicio_d_v(matrizA, matrizB))

    print(ejercicio_e_i_min(matrizA, matrizB))
    print(ejercicio_e_i_max(matrizA, matrizB))
    print(ejercicio_e_ii_min(matrizA, matrizB))
    print(ejercicio_e_ii_max(matrizA, matrizB))
    print(ejercicio_e_iii_min(matrizA, matrizB))
    print(ejercicio_e_iii_max(matrizA, matrizB))
    print(ejercicio_e_iv_min(matrizA, matrizB))
    print(ejercicio_e_iv_max(matrizA, matrizB))
    print(ejercicio_e_v_min(matrizA, matrizB))
    print(ejercicio_e_v_max(matrizA, matrizB))

    print(ejercicio_f_i_min(matrizA, matrizB))
    print(ejercicio_f_i_max(matrizA, matrizB))
    print(ejercicio_f_ii_min(matrizA, matrizB))
    print(ejercicio_f_ii_max(matrizA, matrizB))
    print(ejercicio_f_iii_min(matrizA, matrizB))
    print(ejercicio_f_iii_max(matrizA, matrizB))
    print(ejercicio_f_iv_min(matrizA, matrizB))
    print(ejercicio_f_iv_max(matrizA, matrizB))
    print(ejercicio_f_v_min(matrizA, matrizB))
    print(ejercicio_f_v_max(matrizA, matrizB))

    return 0

main()