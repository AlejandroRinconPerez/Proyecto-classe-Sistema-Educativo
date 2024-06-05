import json

Trainers = []

RUTA_ARCHIVO = "D_Trainers.json"

def guardar_datos_Trainers(trainers):
    global RUTA_ARCHIVO
    try:
        contenido = json.dumps(trainers, indent=4)
        with open(RUTA_ARCHIVO, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")

def cargar_datos_trainers():
    global RUTA_ARCHIVO
    Trainers = []
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            datos = json.load(file)
            if isinstance(datos, list):
                for trainer in datos:
                    Trainers.append(trainer)

        print("Datos cargados exitosamente!!")
        return Trainers
    except Exception:
        print("Error al cargar datos")
        return []
    