def mostrar_tarea ():
    import json
    try: 
        with open("tareas.json", "r") as archivo:
            tareas = json.load(archivo)
            if not tareas:
                print("No hay tareas disponibles.")
                return
    except FileNotFoundError:
        print("El archivo de tareas no se encuentra disponible.")
        return
    print ("---------------Lista de tareas---------------")
    for id_tarea, info in tareas.items():
        print(f"🆔 Tarea #{id_tarea}")
        print(f"📌 Nombre      : {info['nombre_tarea']}")
        print(f"📝 Descripción : {info['descripcion_tarea']}")
        print(f"📅 Fecha       : {info['fecha_tarea']}")
        print("-" * 30)
    print ("---------------Fin de la lista---------------")
mostrar_tarea()