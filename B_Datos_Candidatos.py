import json

Candidatos = []

RUTA_ARCHIVO = "B_Candidatos.json"

def guardar_datos_Candidatos(candidatos):
    global RUTA_ARCHIVO
    try:
        contenido = json.dumps(candidatos, indent=4)
        with open(RUTA_ARCHIVO, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")

def cargar_datos_candidatos():
    global RUTA_ARCHIVO
    Candidatos = []
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            datos = json.load(file)
            if isinstance(datos, list):
                for candidato in datos:
                    Candidatos.append(candidato)

        print("Datos cargados exitosamente!!")
        return Candidatos
    except Exception:
        print("Error al cargar datos")
        return []
    