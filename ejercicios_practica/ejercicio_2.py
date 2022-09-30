# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

def promedio(numeros):
    print("Funcion promedio")
    # La función promedio recibe como parámetro una
    # lista de números. Con ella calcule el promedio como:

    # promedio = sumatoria_numeros / cantidad_numeros 

    # Resuelva la sumatoria y la cantidad con las herramientas
    # que desee, recomendamos usar las funciones disponibles
    # de Python para ello:    
    # sum --> obtener la sumatoria de números
    # len --> obtener la cantidad de números

    # La función debe retornar (return) el promedio calculado
    # La función debe contemplar si se le pasa una lista vacia
    # (es decir, de "0" elementos)
    
    if len(numeros) == 0:  # compruebo si la lista esta vacia 
        resultado = 0
    else:
        sumatoria_numeros = sum(numeros)
        cantidad_numeros = len(numeros)
        promedio = sumatoria_numeros / cantidad_numeros
        resultado = promedio 
    
    return resultado


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    numeros = [2, 4, 6, 8, 10, 12]
    #numeros = []

    # Alumno: Complete la función "promedio"

    # Llamar a la función en este lugar y capturar el valor del retorno
    resultado_promedio = promedio(numeros)

    # Luego imprimir en pantalla el valor resultante:
    # print(....)

    print('El promedio es:', resultado_promedio)

    print("terminamos")