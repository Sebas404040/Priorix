def menuprincipal():
    from creacion_tarea import crear_tarea
    print("1. Crear tarea")
    print("2. Mostrar tareas")
    print("3.Mostrar tareas para hoy")
    print("4.modificar tarea")
    print("5.Eliminar tarea")
    print("6.Salir")
    print("---------------Selecciona una opción---------------")
    print("Selecciona una opción: ", end="")
    try:
        opcion= int(input())
        if opcion < 1 or opcion > 6:
            print("---------------Opción no válida, Intenta de nuevo---------------")
            return menuprincipal()
        if opcion == 1:
            print("Crear tarea")
            crear_tarea()
        elif opcion == 2:   
            print("Mostrar tareas")
        elif opcion == 3:
            print("Mostrar tareas para hoy")
        elif opcion == 4:
            print("Modificar tarea")
        elif opcion == 5:
            print("Eliminar tarea")
        elif opcion == 6:
            print("Salir")
    except ValueError:
        print("---------------Entrada no válida. Por favor, ingresa un número---------------")
        return menuprincipal()
    
