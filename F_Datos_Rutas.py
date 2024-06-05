import json

rutas = []

RUTA_ARCHIVO = "F_Rutas.json"

def guardar_datos_rutas(rutas):
    global RUTA_ARCHIVO
    try:
        contenido = json.dumps(rutas, indent=4)
        with open(RUTA_ARCHIVO, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")

def cargar_datos_rutas():
    global RUTA_ARCHIVO
    rutas = []
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            datos = json.load(file)
            if isinstance(datos, list):
                for ruta in datos:
                    rutas.append(ruta)

        print("Datos cargados exitosamente!!")
        return rutas
        
    except Exception:
        print("Error al cargar datos")
        return []
    

    