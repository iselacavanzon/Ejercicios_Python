estudiantes = {}
opcion = ''
while opcion != '5':
    if opcion == '1':
        nif = input('Ingresa clave del estudiante a registrar: ')
        nombre = input('Ingresa el nombre del estudiante: ')
        calificacion = input('Ingresa la calificación: ')
        estudiante = {'nombre':nombre, 'calificación':calificacion}
        estudiantes[nif] = estudiante
    if opcion == '2':
        nif = input('Introduce clave del estudiante a eliminar: ')
        if nif in estudiantes:
            del estudiantes[nif]
        else:
            print('No existe el estudiante con la clave: ', nif)
    if opcion == '3':
        nif = input('Introduce la clave del estudiante a buscar: ')
        if nif in estudiantes:
            print('Clave de estudiante:', nif)
            for clave, valor in estudiantes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el estudiante con la clave: ', nif)
    if opcion == '4':
        print('Lista de estudiantes:')
        for clave, valor in estudiantes.items():
            print(clave, valor['nombre'], calificacion)

    opcion = input('Elige una opcion:\n(1) Añadir estudiante\n(2) Eliminar estudiante\n(3) Buscar estudiante\n(4) Lista de estudiantes\n(5) Terminar\nElige una opción:')
