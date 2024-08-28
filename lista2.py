sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
for i in sample:
    sum += i

print ("La lista de numeros es: ", sample)
print ("La longitud de la lista es: ", n)
print ("La suma de los numeros en la lista es: ", sum)

x = input ("Ingresa un numero para verificar si se encuentra en la lista: ")
if x in sample:
    print ("el numero: ",x,"se encuentra en la lista")
else:
    print ("el numero: ",x,"no se encuentra en la lista")