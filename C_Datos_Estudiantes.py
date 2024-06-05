import json

Estudiantes = []

RUTA_ARCHIVO = "C_Registro_Estudiantes.json"

def guardar_datos_Estudiantes(estudiantes):
    global RUTA_ARCHIVO
    try:
        contenido = json.dumps(estudiantes, indent=4)
        with open(RUTA_ARCHIVO, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")

def cargar_datos_estudiantes():
    global RUTA_ARCHIVO
    Estudiantes = []
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            datos = json.load(file)
            if isinstance(datos, list):
                for estudiante in datos:
                    Estudiantes.append(estudiante)

        print("Datos cargados exitosamente!!")
        return Estudiantes
    except Exception:
        print("Error al cargar datos")
        return []
    

    