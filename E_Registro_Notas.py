from E_Datos_Notas import*
from C_Registro_Estudiantes import*
from F_Datos_Rutas import*
from F_Registro_Rutas import*
def Modulos_Elegir ():
    try: 
        print(" ----------------------------")
        modulos = ["1. Para Fundamentos de programacion", 
                   "2. Para Programacion Web ",  "3. Para Programación formal",
                    "4. Para Bases de datos" , " 5. Para Backend"]
        for i in modulos:       
            print(i)
        op = int(input("ingrese la opcion deseada ="))   
        if op == 1:
            modulo = "Para Programacion Web" 
        elif op == 2:
            modulo = "Fundamentos de programacion"
        elif op == 3:
            modulo = " Programación formal"
        elif op == 4:
            modulo = "Para Bases de datos"
        elif op == 5:
            modulo = "Para Backend"
        else:
            print("No valido")
            return
        return  modulo
                                
    except Exception as e:
                print(f"Se ha producido un error: {e}")
                print("Por favor, intente nuevamente.")
########################################################################





        

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

def Registro_moduloXX():
    
            rutas = cargar_datos_rutas()
            
            print("-------------------------------------------------")
            print("Una vez culminado el modulo agregue todas las notas")
            doc = input("Ingrese numero de documento del estudiante:  ")
            hora =  salon_Hotario()
            Nombre_Grupo = input("Ingrese grupo, ej. U2, U1, A2: ")
            modulo = Modulos_Elegir()
            
            notas_modulo = {}
            notas_modulo["QuiZ#1"] = int(input("Ingrese la Nota del Quiz#1:  ")) 
            notas_modulo["QuiZ#2"] = int(input("Ingrese la Nota del Quiz#2:  "))
            notas_modulo["Tarea#1"] = int(input("Ingrese la Nota del Tarea#1:  "))
            notas_modulo["Tarea#2"] = int(input("Ingrese la Nota del Tarea#2:  "))
            notas_modulo["Proyecto"] = int(input("Ingrese la Nota del Proyecto:  "))
            notas_modulo["Evaluacion"] = int(input("Ingrese la Nota del Evaluacion:  "))
            ###############################################################################
            #Calculo de nota final 
            notas10 = ((notas_modulo["QuiZ#1"] + notas_modulo["QuiZ#2"] + notas_modulo["Tarea#1"] +notas_modulo["Tarea#2"] )/4)*0.10
            notas30 = notas_modulo["Evaluacion"] *0.30
            notas60 = notas_modulo["Proyecto"] *0.60
            notas_modulo["Nota final"]= notas10 + notas30 + notas60
            ###############################################################################
            #risk evaluaation to double check 
            
            if notas_modulo["Nota final"] < 60:
                        notas_modulo["Riesgo"]= "Riesgo Alto"
            elif  notas_modulo["Nota final"] > 59:
                        notas_modulo["Riesgo"]= "No esta Riesgo"
            # to add the info to the dict 
            for ruta in rutas:
                if hora in ruta:
                    if Nombre_Grupo in ruta[hora]:
                        if "Aula" in ruta[hora][Nombre_Grupo]:
                            if doc in ruta[hora][Nombre_Grupo]["Aula"]:
                                if modulo not in ruta[hora][Nombre_Grupo]["Aula"][doc]:
                                    ruta[hora][Nombre_Grupo]["Aula"][doc][modulo] = {}
                                ruta[hora][Nombre_Grupo]["Aula"][doc][modulo] = notas_modulo
                                return
            
                print("No se encontró el estudiante en la ruta especificada.")
            guardar_datos_rutas(rutas)
            guardar_datos_rutas(rutas)
       
    
def Calculo_Riesgo():
    rutas = cargar_datos_rutas()
    modulo = Modulos_Elegir()

    if modulo:
        print("-------------------------------------------------")
        print(f"Cargando estudiantes con riesgo alto en el módulo {modulo}")
        for ruta in rutas:
            for hora, grupos in ruta.items():
                if "Aula" in grupos:
                    for grupo, estudiantes in grupos["Aula"].items():
                        for estudiante_id, estudiante_info in estudiantes.items():
                            if modulo in estudiante_info and estudiante_info[modulo]["Riesgo"] == "Riesgo Alto":
                                print(f"Estudiante: {estudiante_info['Nombre']} {estudiante_info['Apellido']} - Riesgo: {estudiante_info[modulo]['Riesgo']}")

    else:
        print("Opción de módulo no válida.")



def Mostrar_Notas_Estudiante():
    rutas = cargar_datos_rutas()

    doc = input("Ingrese número de documento del estudiante: ")
    hora = salon_Hotario()
    Nombre_Grupo = input("Ingrese grupo, ej. U2, U1, A2: ")

    for ruta in rutas:
        if hora in ruta:
            if Nombre_Grupo in ruta[hora]:
                if "Aula" in ruta[hora][Nombre_Grupo]:
                    if doc in ruta[hora][Nombre_Grupo]["Aula"]:
                        estudiante = ruta[hora][Nombre_Grupo]["Aula"][doc]
                        print(f"Notas del estudiante {estudiante['Nombre']} {estudiante['Apellido']}:")
                        for modulo, notas_modulo in estudiante.items():
                            if modulo not in ['Nombre', 'Apellido', 'Telefono', 'Direccion', 'Acudiente', 'Estado', 'Ruta', 'Horario', 'Profesor']:
                                print(f"\nMódulo: {modulo}")
                                for clave, valor in notas_modulo.items():
                                    if clave != "Riesgo":
                                        print(f"{clave}: {valor}")
                        return

    print("No se encontró el estudiante en la ruta especificada.")

# Llamada a la función
#Mostrar_Notas_Estudiante()

#Registro_moduloXX()
            
            
           
    
    

#Registro_moduloXX()