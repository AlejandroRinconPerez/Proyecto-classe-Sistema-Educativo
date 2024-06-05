import json

Notas = []

RUTA_ARCHIVO = "E_Notas.json"

def guardar_datos_notas(notas):
    global RUTA_ARCHIVO
    try:
        contenido = json.dumps(notas, indent=4)
        with open(RUTA_ARCHIVO, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")

def cargar_datos_notas():
    global RUTA_ARCHIVO
    Notas = []
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            datos = json.load(file)
            if isinstance(datos, list):
                for nota in datos:
                    Notas.append(nota)

        print("Datos cargados exitosamente!!")
        return Notas
    except Exception:
        print("Error al cargar datos")
        return []
    