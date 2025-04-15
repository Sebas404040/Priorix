def modificar_tarea():
    print ("---------------Modificar tarea---------------")
    import json
    try:
        with open("tareas.json", "r") as file:
            tareas = json.load(file)
    except FileNotFoundError:
        print("El archivo de tareas no se encuentra disponible.")
        return
    if not tareas:
        print("No hay tareas disponibles.")
        return
    print ("---------------Lista de tareas---------------")
    for id_tarea, info in tareas.items():
        print(f"🆔 Tarea #{id_tarea}")
        print(f"📌 Nombre      : {info['nombre_tarea']}")
        print(f"📝 Descripción : {info['descripcion_tarea']}")
        print(f"📅 Fecha       : {info['fecha_tarea']}")
        print("-" * 30)
    print ("---------------Fin de la lista---------------")
    print("Selecciona el ID de la tarea que deseas modificar: ", end="")
    try:
        id_tarea_modificar = input()
        if id_tarea_modificar not in tareas:
            print("ID de tarea no válido.")
            return modificar_tarea()
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")
        return modificar_tarea()
    print("Selecciona el campo que deseas modificar:")
    print("1. Nombre de la tarea")
    print("2. Descripción de la tarea")
    print("3. Fecha de la tarea")
    print("4. Salir")
    print("Selecciona una opción: ", end="")
    try:
        opcion_modificar = int(input())
        if opcion_modificar < 1 or opcion_modificar > 4:
            print("Opción no válida. Intenta de nuevo.")
            return modificar_tarea()
        if opcion_modificar == 1:
            nuevo_nombre = input("Nuevo nombre de la tarea: ")
            tareas[id_tarea_modificar]['nombre_tarea'] = nuevo_nombre
        elif opcion_modificar == 2:
            nueva_descripcion = input("Nueva descripción de la tarea: ")
            tareas[id_tarea_modificar]['descripcion_tarea'] = nueva_descripcion
        elif opcion_modificar == 3:
            nueva_fecha = input("Nueva fecha de la tarea (YYYY-MM-DD): ")
            tareas[id_tarea_modificar]['fecha_tarea'] = nueva_fecha
        elif opcion_modificar == 4:
            print("Salir")
            return
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")
        return modificar_tarea()
    with open("tareas.json", "w") as file:
        json.dump(tareas, file, indent=4)
    print("Tarea modificada con éxito.")
    print("------------------------------")
    from main import menuprincipal
    menuprincipal()

def eliminar_tarea():
    from main import menuprincipal
    print ("---------------Eliminar tarea---------------")
    import json
    try:
        with open("tareas.json", "r") as file:
            tareas = json.load(file)
    except FileNotFoundError:
        print("El archivo de tareas no se encuentra disponible.")
        return
    if not tareas:
        print("No hay tareas disponibles.")
        return
    print ("---------------Lista de tareas---------------")
    for id_tarea, info in tareas.items():
        print(f"🆔 Tarea #{id_tarea}")
        print(f"📌 Nombre      : {info['nombre_tarea']}")
        print(f"📝 Descripción : {info['descripcion_tarea']}")
        print(f"📅 Fecha       : {info['fecha_tarea']}")
        print("-" * 30)
    print ("---------------Fin de la lista---------------")
    print("Selecciona el ID de la tarea que deseas eliminar: ", end="")
    try:
        id_tarea_eliminar = input()
        if id_tarea_eliminar not in tareas:
            print("ID de tarea no válido.")
            return eliminar_tarea()
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")
        return eliminar_tarea()
    del tareas[id_tarea_eliminar]
    with open("tareas.json", "w") as file:
        json.dump(tareas, file, indent=4)
    print("Tarea eliminada con éxito.")
    print("------------------------------")
    menuprincipal()

