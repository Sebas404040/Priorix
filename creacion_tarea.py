def crear_tarea():
    from main import menuprincipal
    import json
    import datetime
    try:
        with open("tareas.json", "r") as file:
            tareas = json.load(file)
    except FileNotFoundError:
        tareas = {}
    print ("---------------Crear tarea---------------")
    numero_tarea = len(tareas) + 1
    nombre_tarea = input("Nombre de la tarea: ")
    descripcion_tarea = input("Descripción de la tarea: ")
    fecha_tarea = datetime.datetime.now().date()
    tarea= {
        "nombre_tarea": nombre_tarea,
        "descripcion_tarea": descripcion_tarea,
        "fecha_tarea": str(fecha_tarea)
    }
    tareas[numero_tarea] = tarea
    with open("tareas.json", "w") as file:
        json.dump(tareas, file, indent=4)
    print("Tarea creada con éxito.")
    print("--------------------------------------")
    menuprincipal()
