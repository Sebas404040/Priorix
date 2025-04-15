def mostrar_tarea ():
    from main import menuprincipal
    import json
    try: 
        with open("tareas.json", "r") as archivo:
            tareas = json.load(archivo)
            if not tareas:
                print("No hay tareas disponibles.")
                menuprincipal()
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
    menuprincipal()

def mostrar_hoy():
    from main import menuprincipal
    import json
    import datetime
    try: 
        with open("tareas.json", "r") as archivo:
            tareas = json.load(archivo)
            if not tareas:
                print("No hay tareas disponibles.")
                menuprincipal()
    except FileNotFoundError:
        print("El archivo de tareas no se encuentra disponible.")
        return
    
    fecha_hoy = datetime.datetime.now().date()
    fecha_hoy = str(fecha_hoy)
    print ("---------------Lista de tareas para hoy---------------")
    for id_tarea, info in tareas.items():
        if info['fecha_tarea'] == fecha_hoy:
            print(f"🆔 Tarea #{id_tarea}")
            print(f"📌 Nombre      : {info['nombre_tarea']}")
            print(f"📝 Descripción : {info['descripcion_tarea']}")
            print(f"📅 Fecha       : {info['fecha_tarea']}")
            print("-" * 30)
    print ("---------------Fin de la lista---------------")
    menuprincipal()