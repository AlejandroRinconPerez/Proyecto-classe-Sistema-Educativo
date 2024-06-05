from E_Datos_Notas import*
from C_Registro_Estudiantes import*
def Registro_modulo_Fundamentos_de_programacioon():
    while True:
        try:
            print("-------------------------------------------------")
            print("Una vez culminado el modulo agregue todas las notas")
            notas = cargar_datos_notas()
            estudiantes = cargar_datos_estudiantes()
            doc = input("Ingrese numero de documento del estudiante:  ")
            Numero_Modulo = input("Ingrese el numero de modulo que quiere ")
            modulo = "Modulo " + Numero_Modulo
        
            for nota in notas:
                if modulo in nota.get(doc, {}):
                    print("Modulo existente")
                    op1 = int(input("Desea sobre escribirlo ? 1. Para SI 2. Para NO: "))
                    if op1 == 2:
                        return
            notas_modulo = {}
            notas_modulo["QuiZ#1"] = int(input("Ingrese la Nota del Quiz#1:  "))
            notas_modulo["QuiZ#2"] = int(input("Ingrese la Nota del Quiz#2:  "))
            notas_modulo["Tarea#1"] = int(input("Ingrese la Nota delTarea#1:  "))
            notas_modulo["Tarea#2"] = int(input("Ingrese la Nota del Tarea#2:  "))
            notas_modulo["Proyecto"] = int(input("Ingrese la Nota delProyecto:  "))
            notas_modulo["Evaluacion"] =int(input("Ingrese la Nota del Evaluacion:  "))
            
            notas10 = ((notas_modulo["QuiZ#1"] + notas_modulo["QuiZ#2"] + notas_modulo["Tarea#1"] +notas_modulo["Tarea#2"] )/4)*0.10
            notas30 = notas_modulo["Evaluacion"] *0.30
            notas60 = notas_modulo["Proyecto"] *0.60
            notas_modulo["Nota final"]= notas10 + notas30 + notas60
            
            if notas_modulo["Nota final"] < 60:
                notas_modulo["Riesgo"]= "Riesgo Alto"
            elif  notas_modulo["Nota final"] > 59:
                notas_modulo["Riesgo"]= "No esta Riesgo"
            notas.append({doc: {modulo: notas_modulo}})
            guardar_datos_notas(notas)
            
            x = notas_modulo["Riesgo"]
            for estudiante in estudiantes:
                if  doc in estudiante:
                    op = int(input("Desea cambiar el Riesgo ? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        estudiante[doc]["Riesgo"] = x
                        guardar_datos_Estudiantes(estudiantes)
                        guardar_datos_notas(notas)
                        notas.append({doc: {modulo: notas_modulo}})
                        return
                    elif op == 2:
                        return
                    else:
                        print("Opción no válida.")
            
            guardar_datos_Estudiantes(estudiantes)
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
def Registro_modulo_Programacion_Web():
    while True:
        try:
            print("-------------------------------------------------")
            print("Una vez culminado el modulo agregue todas las notas")
            notas = cargar_datos_notas()
            estudiantes = cargar_datos_estudiantes()
            doc = input("Ingrese numero de documento del estudiante:  ")
            Numero_Modulo = input("Ingrese el numero de modulo que quiere ")
            modulo = "Modulo " + Numero_Modulo
        
            for nota in notas:
                if modulo in nota.get(doc, {}):
                    print("Modulo existente")
                    op1 = int(input("Desea sobre escribirlo ? 1. Para SI 2. Para NO: "))
                    if op1 == 2:
                        return
            notas_modulo = {}
            notas_modulo["QuiZ#1"] = int(input("Ingrese la Nota del Quiz#1:  "))
            notas_modulo["QuiZ#2"] = int(input("Ingrese la Nota del Quiz#2:  "))
            notas_modulo["Tarea#1"] = int(input("Ingrese la Nota delTarea#1:  "))
            notas_modulo["Tarea#2"] = int(input("Ingrese la Nota del Tarea#2:  "))
            notas_modulo["Proyecto"] = int(input("Ingrese la Nota delProyecto:  "))
            notas_modulo["Evaluacion"] =int(input("Ingrese la Nota del Evaluacion:  "))
            
            notas10 = ((notas_modulo["QuiZ#1"] + notas_modulo["QuiZ#2"] + notas_modulo["Tarea#1"] +notas_modulo["Tarea#2"] )/4)*0.10
            notas30 = notas_modulo["Evaluacion"] *0.30
            notas60 = notas_modulo["Proyecto"] *0.60
            notas_modulo["Nota final"]= notas10 + notas30 + notas60
            
            if notas_modulo["Nota final"] < 60:
                notas_modulo["Riesgo"]= "Riesgo Alto"
            elif  notas_modulo["Nota final"] > 59:
                notas_modulo["Riesgo"]= "No esta Riesgo"
            notas.append({doc: {modulo: notas_modulo}})
            guardar_datos_notas(notas)
            
            x = notas_modulo["Riesgo"]
            for estudiante in estudiantes:
                if  doc in estudiante:
                    op = int(input("Desea cambiar el Riesgo ? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        estudiante[doc]["Riesgo"] = x
                        guardar_datos_Estudiantes(estudiantes)
                        guardar_datos_notas(notas)
                        notas.append({doc: {modulo: notas_modulo}})
                        return
                    elif op == 2:
                        return
                    else:
                        print("Opción no válida.")
            
            guardar_datos_Estudiantes(estudiantes)
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
def Registro_modulo_Programacioon_formal():
    while True:
        try:
            print("-------------------------------------------------")
            print("Una vez culminado el modulo agregue todas las notas")
            notas = cargar_datos_notas()
            estudiantes = cargar_datos_estudiantes()
            doc = input("Ingrese numero de documento del estudiante:  ")
            Numero_Modulo = input("Ingrese el numero de modulo que quiere ")
            modulo = "Modulo " + Numero_Modulo
        
            for nota in notas:
                if modulo in nota.get(doc, {}):
                    print("Modulo existente")
                    op1 = int(input("Desea sobre escribirlo ? 1. Para SI 2. Para NO: "))
                    if op1 == 2:
                        return
            notas_modulo = {}
            notas_modulo["QuiZ#1"] = int(input("Ingrese la Nota del Quiz#1:  "))
            notas_modulo["QuiZ#2"] = int(input("Ingrese la Nota del Quiz#2:  "))
            notas_modulo["Tarea#1"] = int(input("Ingrese la Nota delTarea#1:  "))
            notas_modulo["Tarea#2"] = int(input("Ingrese la Nota del Tarea#2:  "))
            notas_modulo["Proyecto"] = int(input("Ingrese la Nota delProyecto:  "))
            notas_modulo["Evaluacion"] =int(input("Ingrese la Nota del Evaluacion:  "))
            
            notas10 = ((notas_modulo["QuiZ#1"] + notas_modulo["QuiZ#2"] + notas_modulo["Tarea#1"] +notas_modulo["Tarea#2"] )/4)*0.10
            notas30 = notas_modulo["Evaluacion"] *0.30
            notas60 = notas_modulo["Proyecto"] *0.60
            notas_modulo["Nota final"]= notas10 + notas30 + notas60
            
            if notas_modulo["Nota final"] < 60:
                notas_modulo["Riesgo"]= "Riesgo Alto"
            elif  notas_modulo["Nota final"] > 59:
                notas_modulo["Riesgo"]= "No esta Riesgo"
            notas.append({doc: {modulo: notas_modulo}})
            guardar_datos_notas(notas)
            
            x = notas_modulo["Riesgo"]
            for estudiante in estudiantes:
                if  doc in estudiante:
                    op = int(input("Desea cambiar el Riesgo ? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        estudiante[doc]["Riesgo"] = x
                        guardar_datos_Estudiantes(estudiantes)
                        guardar_datos_notas(notas)
                        notas.append({doc: {modulo: notas_modulo}})
                        return
                    elif op == 2:
                        return
                    else:
                        print("Opción no válida.")
            
            guardar_datos_Estudiantes(estudiantes)
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
def Registro_modulo_Bases_de_datos():
    while True:
        try:
            print("-------------------------------------------------")
            print("Una vez culminado el modulo agregue todas las notas")
            notas = cargar_datos_notas()
            estudiantes = cargar_datos_estudiantes()
            doc = input("Ingrese numero de documento del estudiante:  ")
            Numero_Modulo = input("Ingrese el numero de modulo que quiere ")
            modulo = "Modulo " + Numero_Modulo
        
            for nota in notas:
                if modulo in nota.get(doc, {}):
                    print("Modulo existente")
                    op1 = int(input("Desea sobre escribirlo ? 1. Para SI 2. Para NO: "))
                    if op1 == 2:
                        return
            notas_modulo = {}
            notas_modulo["QuiZ#1"] = int(input("Ingrese la Nota del Quiz#1:  "))
            notas_modulo["QuiZ#2"] = int(input("Ingrese la Nota del Quiz#2:  "))
            notas_modulo["Tarea#1"] = int(input("Ingrese la Nota delTarea#1:  "))
            notas_modulo["Tarea#2"] = int(input("Ingrese la Nota del Tarea#2:  "))
            notas_modulo["Proyecto"] = int(input("Ingrese la Nota delProyecto:  "))
            notas_modulo["Evaluacion"] =int(input("Ingrese la Nota del Evaluacion:  "))
            
            notas10 = ((notas_modulo["QuiZ#1"] + notas_modulo["QuiZ#2"] + notas_modulo["Tarea#1"] +notas_modulo["Tarea#2"] )/4)*0.10
            notas30 = notas_modulo["Evaluacion"] *0.30
            notas60 = notas_modulo["Proyecto"] *0.60
            notas_modulo["Nota final"]= notas10 + notas30 + notas60
            
            if notas_modulo["Nota final"] < 60:
                notas_modulo["Riesgo"]= "Riesgo Alto"
            elif  notas_modulo["Nota final"] > 59:
                notas_modulo["Riesgo"]= "No esta Riesgo"
            notas.append({doc: {modulo: notas_modulo}})
            guardar_datos_notas(notas)
            
            x = notas_modulo["Riesgo"]
            for estudiante in estudiantes:
                if  doc in estudiante:
                    op = int(input("Desea cambiar el Riesgo ? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        estudiante[doc]["Riesgo"] = x
                        guardar_datos_Estudiantes(estudiantes)
                        guardar_datos_notas(notas)
                        notas.append({doc: {modulo: notas_modulo}})
                        return
                    elif op == 2:
                        return
                    else:
                        print("Opción no válida.")
            
            guardar_datos_Estudiantes(estudiantes)
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
def Registro_modulo_Backend():
    while True:
        try:
            print("-------------------------------------------------")
            print("Una vez culminado el modulo agregue todas las notas")
            notas = cargar_datos_notas()
            estudiantes = cargar_datos_estudiantes()
            doc = input("Ingrese numero de documento del estudiante:  ")
            Numero_Modulo = input("Ingrese el numero de modulo que quiere ")
            modulo = "Modulo " + Numero_Modulo
        
            for nota in notas:
                if modulo in nota.get(doc, {}):
                    print("Modulo existente")
                    op1 = int(input("Desea sobre escribirlo ? 1. Para SI 2. Para NO: "))
                    if op1 == 2:
                        return
            notas_modulo = {}
            notas_modulo["QuiZ#1"] = int(input("Ingrese la Nota del Quiz#1:  "))
            notas_modulo["QuiZ#2"] = int(input("Ingrese la Nota del Quiz#2:  "))
            notas_modulo["Tarea#1"] = int(input("Ingrese la Nota delTarea#1:  "))
            notas_modulo["Tarea#2"] = int(input("Ingrese la Nota del Tarea#2:  "))
            notas_modulo["Proyecto"] = int(input("Ingrese la Nota delProyecto:  "))
            notas_modulo["Evaluacion"] =int(input("Ingrese la Nota del Evaluacion:  "))
            
            notas10 = ((notas_modulo["QuiZ#1"] + notas_modulo["QuiZ#2"] + notas_modulo["Tarea#1"] +notas_modulo["Tarea#2"] )/4)*0.10
            notas30 = notas_modulo["Evaluacion"] *0.30
            notas60 = notas_modulo["Proyecto"] *0.60
            notas_modulo["Nota final"]= notas10 + notas30 + notas60
            
            if notas_modulo["Nota final"] < 60:
                notas_modulo["Riesgo"]= "Riesgo Alto"
            elif  notas_modulo["Nota final"] > 59:
                notas_modulo["Riesgo"]= "No esta Riesgo"
            notas.append({doc: {modulo: notas_modulo}})
            guardar_datos_notas(notas)
            
            x = notas_modulo["Riesgo"]
            for estudiante in estudiantes:
                if  doc in estudiante:
                    op = int(input("Desea cambiar el Riesgo ? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        estudiante[doc]["Riesgo"] = x
                        guardar_datos_Estudiantes(estudiantes)
                        guardar_datos_notas(notas)
                        notas.append({doc: {modulo: notas_modulo}})
                        return
                    elif op == 2:
                        return
                    else:
                        print("Opción no válida.")
            
            guardar_datos_Estudiantes(estudiantes)
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")

            
def ver_notas_por_estudiante ():
    while True:
        try:
            notas = cargar_datos_notas()
            doc = input("Ingrese numero de documento del estudiante:  ")
            Numero_Modulo = input("Ingrese el numero de modulo que quiere ")
            modulo = "Modulo " + Numero_Modulo
            for nota in notas:
                if doc in nota and modulo in nota[doc]:
                    print(f"El estudiante con documento {doc} en el {modulo} tiene las siguientes notas:")
                    for llave, valor in nota[doc][modulo].items():
                        print(f"{llave}: {valor}")
                    return
            print("El documento o el módulo no existen.")
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")      
            
#Registro_modulo ()
#ver_notas_por_estudiante ()


    