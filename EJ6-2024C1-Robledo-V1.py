''''
Hallar sen (pi/3) con un error relativo menor al 0.01% utilizando la siguiente expansión en
serie
$C(x)=\sum_{i=1}^{\infty}(-1)^{i+1} \frac{x^{2 i-1}}{(2 i-1) !}$
'''
SENO_DE_PI_SOBRE_TRES = 0.86602540378445
ERROR_OBJETIVO = 0.0001
PI = 3.1415926535897932384
def expancion_en_serie (x, i):
    i += 1
    resultado = (-1) ** (i+1) * (x ** (2*i - 1) / factorial(2*i - 1))
    return resultado

def factorial (x):
    resultado = 1
    for i in range (0, x):
        resultado *= (i + 1)
    return resultado

def absoluto (x):
    resultado = 0
    if x > 0:
        resultado = x
    elif x < 0 :
        resultado = (-1) * x
    return resultado

def calcular_seno_pi_sobre_tres ():
    resultado_aproximado = expancion_en_serie(PI/3, 0)
    iteracion = 1
    while calcular_error_relativo(resultado_aproximado, SENO_DE_PI_SOBRE_TRES) > ERROR_OBJETIVO:
        resultado_aproximado += expancion_en_serie(PI/3, iteracion)
        iteracion += 1
    return resultado_aproximado

def calcular_error_relativo(aproximacion, valor_exacto):
    error = (absoluto(aproximacion - valor_exacto)) / valor_exacto
    return error


def main():

    print(calcular_seno_pi_sobre_tres())
    return 0

main()