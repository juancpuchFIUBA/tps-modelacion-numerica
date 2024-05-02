def gauss_seidel(A, b, x0, tol, max_iter):
    # Obtenemos la dimensión de la matriz A
    n = len(b)
    # Copiamos el vector inicial x0 para no modificarlo
    x = x0.copy()
    # Creamos un vector para almacenar la nueva iteración de x
    x_new = np.zeros(n)
    # Inicializamos el contador de iteraciones
    iter_count = 0

    # Iteramos hasta que se cumpla alguna condición de parada
    while True:
        # Iteramos sobre cada fila de la matriz A
        for i in range(n):
            # Calculamos la nueva iteración de x[i]
            x_new[i] = (b[i] - np.dot(A[i, :i], x_new[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

        # Comprobamos si la norma de la diferencia entre x y x_new es menor que la tolerancia
        # o si hemos alcanzado el número máximo de iteraciones
        if np.linalg.norm(x_new - x) < tol or iter_count >= max_iter:
            # Si se cumple alguna de las condiciones, salimos del bucle
            break

        # Actualizamos x con la nueva iteración calculada
        x = x_new.copy()
        # Incrementamos el contador de iteraciones
        iter_count += 1

    # Devolvemos la solución encontrada y el número de iteraciones realizadas
    return x_new, iter_count


