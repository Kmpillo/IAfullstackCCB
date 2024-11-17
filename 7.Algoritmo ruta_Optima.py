import heapq

# Direcciones en las que nos podemos mover: arriba, abajo, izquierda, derecha.
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movimientos: arriba, abajo, izquierda, derecha

def max_sum_path(matrix, start, end):
    n = len(matrix)
    
    # Cola de prioridad: almacenará elementos en la forma (-suma_acumulada, x, y)
    pq = []
    heapq.heappush(pq, (-matrix[start[0]][start[1]], start[0], start[1]))  # Empezamos con el valor de la celda de inicio
    
    # Matriz para almacenar la máxima suma alcanzada hasta cada celda
    max_sum = [[-float('inf')] * n for _ in range(n)]
    max_sum[start[0]][start[1]] = matrix[start[0]][start[1]]  # El valor inicial es el de la celda de inicio
    
    # Matriz para almacenar las posiciones recorridas
    parent = [[None] * n for _ in range(n)]  # Para reconstruir el camino más tarde
    path = []  # Para guardar el camino recorrido
    
    while pq:
        # Extraer el nodo con la mayor suma acumulada
        current_sum, x, y = heapq.heappop(pq)
        current_sum = -current_sum  # Convertimos el valor de nuevo a positivo
        
        # Si hemos llegado al destino, devolvemos la suma máxima y el camino
        if (x, y) == end:
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[x][y]
            path.append(start)
            path.reverse()  # Invertir el camino para mostrarlo de inicio a fin
            return current_sum, path
        
        # Explorar los vecinos
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Asegurarnos de que estamos dentro de los límites de la matriz
            if 0 <= nx < n and 0 <= ny < n:
                new_sum = current_sum + matrix[nx][ny]
                
                # Si encontramos una suma mayor para llegar a (nx, ny), actualizamos y añadimos a la cola
                if new_sum > max_sum[nx][ny]:
                    max_sum[nx][ny] = new_sum
                    parent[nx][ny] = (x, y)  # Guardamos la posición del padre (de donde venimos)
                    heapq.heappush(pq, (-new_sum, nx, ny))
    
    # Si no se encuentra ruta, retornar -1 o un valor adecuado
    return -1, []

def main():
    # 1. Leer las dimensiones de la matriz
    n = int(input("Ingrese el tamaño de la matriz n x n: "))
    
    # 2. Crear y llenar la matriz con los valores proporcionados por el usuario
    matrix = []
    print(f"Ingrese los valores para la matriz {n}x{n}:")
    for i in range(n):
        row = []
        for j in range(n):
            valor = int(input(f"Valor en posición ({i}, {j}): "))
            row.append(valor)
        matrix.append(row)
    
    # 3. Leer las posiciones de salida y llegada
    print("Ingrese la posición de salida:")
    start_x = int(input("Fila de la posición de salida: "))
    start_y = int(input("Columna de la posición de salida: "))
    
    print("Ingrese la posición de llegada:")
    end_x = int(input("Fila de la posición de llegada: "))
    end_y = int(input("Columna de la posición de llegada: "))
    
    start = (start_x, start_y)
    end = (end_x, end_y)
    
    # 4. Encontrar la ruta con la mayor suma
    resultado, path = max_sum_path(matrix, start, end)
    
    # 5. Esperar la orden para mostrar el resultado
    print("\nIngrese '1' para mostrar el resultado o cualquier otra tecla para salir.")
    orden = input()
    
    if orden == '1':
        if resultado != -1:
            print(f"La mayor suma posible en el camino es: {resultado}")
            print("Posiciones recorridas:")
            for pos in path:
                print(f"Posición: {pos} con valor: {matrix[pos[0]][pos[1]]}")
        else:
            print("No existe un camino válido desde la posición de salida hasta la de llegada.")
    else:
        print("Programa terminado sin mostrar el resultado.")

if __name__ == "__main__":
    main()
