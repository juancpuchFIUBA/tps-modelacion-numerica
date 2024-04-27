import math

def C(x, n):
    result = 0
    for i in range(1, n+1):
        result += (-1)**(i+1) * (x**(2*i-1)) / math.factorial(2*i-1)
    return result

exacto = math.sin(math.pi/3)
n = 1
error = 1
while error > 0.0001:
    aproximado = C(math.pi/3, n)
    error = abs((exacto - aproximado) / exacto)
    n += 1

print("Número de términos necesarios:", n)
print("Valor aproximado:", aproximado)
print("Error relativo:", error)


