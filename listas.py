Numeros = []
i = 5    # cantida de numeros pedido
ejercicio = {}    # Diccionario que tendra lo pedido
for cont in range(i):   # un ciclo for para llenar la lista de Numeros
    entrada = input("ingresa un numero entero: ")
    if entrada.isdigit() == False:   #comprueba si es un string que pueda ser numero
        while entrada.isdigit() == False:   # while  hasta quese ingrese un numero valido
            entrada = input("No ingreso un numero, por favor escriba un numero ")
        Numeros.append(int(entrada))    # agregar el valor a lista y convertido en entero
    else:
        Numeros.append(int(entrada)) 
ejercicio["Numeros"] = Numeros

print("La lista de numeros es: ", Numeros)