from C_Datos_Estudiantes import*
from B_Registro_candidatos import*
from B_Datos_Candidatos import*

def Registro_de_estudiantes():
    print("------------------------------------------")
    while True:
        try:
            estudiantes = cargar_datos_estudiantes()
            candidatos = cargar_datos_candidatos()
            
            doc = input("Ingrese numero de documento del estudiante:  ")
            for estudiante in estudiantes:
                if estudiante.get(doc,None) != None:
                    # candidatos[i][doc]["estado"]=nuevo
                    print("Estudiante ha sido registrado anteriormente")
                    return
            Personales_estudiante = {}
            print("Para continuar Validaremos si el candidato aprobo")
            for candidato in candidatos:
                if doc in candidato:
                    Teorico=  candidato[doc]["Nota examen Teorico"]#possible error 
                    practico= candidato[doc]["Nota examen practico"]
                    x = (Teorico + practico) / 2 
                    if x < 59:
                        print(" Candidato no aprobo")
                        return     
            print("Candidato si aprobo Puede registrar sus datos")
            Personales_estudiante["Nombre"] = input("Ingrese el nombre:  ")
            Personales_estudiante["Apellido"] = input("Ingrese el Apellido:  ")
            Personales_estudiante["Telefono"] = input("Ingrese el Telefono:  ")
            Personales_estudiante["Direccion"] = input("Ingrese la Direccion:  ")
            Personales_estudiante["Acudiente"] = input("Nombre Acudiente:  ")
            Personales_estudiante["Estado"] = input("Entre Aprobado,Cursando, Graduado, Expulsado, Retirado Elija:  ")
            Personales_estudiante["Riesgo"] = "No esta Riesgo"
            # Personales_estudiante["Ruta"] = None
            # Personales_estudiante["Horario"] = None
            # Personales_estudiante["Profesor"] =None
            estudiante = {}
            estudiante[doc]=Personales_estudiante
            #agreaggr el horario a la info personal
            
            estudiantes.append(estudiante)
            guardar_datos_Estudiantes(estudiantes)
            print("----------------------------------------------------------")
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
def listar_campers ():
    while True:
        try:
            estudiantes = cargar_datos_estudiantes()
            cantidad = len(estudiantes)
            print ( f"La cantidad de campers inscritos en todos los cursos es:{cantidad}")
            for estudiante in estudiantes:
                print("\n Datos de estudiantes")
                for llave,  valor in estudiante.items():
                    print (f"Estudiante con documento {llave} tiene los siguientes datos {valor}")
            break
            #imprimir la listae campers
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
def cambiar_estado_camper():
    while True:
        try:
            estudiantes = cargar_datos_estudiantes()
            doc = input("Ingrese numero de documento del estudiante:  ")
            for estudiante in estudiantes:
                if  doc in estudiante:
                    op = int(input("Desea cambiar el estado? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        estudiante[doc]["Estado"] = input("Ingrese el nuevo estado (Aprobado, Cursando, Graduado, Expulsado, Retirado): ")
                        print("Estado actualizado correctamente.")
                        guardar_datos_Estudiantes(estudiantes)
                        return
                    elif op == 2:
                        return
                    else:
                        print("Opción no válida.")
                        return
                
            print("Estudiante no registrado.")
            break#aparece por que si  
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
def cambiar_riesgo_camper():
    while True:
        try:
    
            estudiantes = cargar_datos_estudiantes()
            doc = input("Ingrese numero de documento del estudiante:  ")
            for estudiante in estudiantes:
                if  doc in estudiante:
                    print (f" el estudiante de {doc} y Nombre {estudiante[doc]['Nombre']} esta {estudiante[doc]['Riesgo']}")
                    return
            print("Estudiante no registrado.")
            break
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
    
def consultar_Camper():
    while True:
        try:
            estudiantes = cargar_datos_estudiantes()
            doc = input("Ingrese numero de documento del estudiante:  ")
            for estudiante in estudiantes:
                if  doc in estudiante:
                    for llave, valor in estudiante.items():
                        print(llave,valor)
                        return
            print("Estudiante no registrado.")   
            break  
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
    
    
def cambiar_infopersonal_camper():
    while True:
        try:
            estudiantes = cargar_datos_estudiantes()
            doc = input("Ingrese numero de documento del estudiante:  ")
            for estudiante in estudiantes:
                if  doc in estudiante:
                    op = int(input("Desea cambiar la informacion personal? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        estudiante[doc]["Nombre"] = input("Actualice el nombre:  ")
                        estudiante[doc]["Apellido"] = input("Actualice el Apellido:  ")
                        estudiante[doc]["Telefono"] = input("Actualice el Telefono:  ")
                        estudiante[doc]["Direccion"] = input("Actualice la Direccion:  ")
                        estudiante[doc]["Acudiente"] = input("Actualice Nombre Acudiente:  ")
                        print("Estado actualizado correctamente.")
                        guardar_datos_Estudiantes(estudiantes)
                        return
                    elif op == 2:
                        return
                    else:
                        print("Opción no válida.")
                        return
            print("Estudiante no registrado.")
            break#aparece por que si 
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
    
    
def Eliminar_camper():
    while True:
        try:
            estudiantes = cargar_datos_estudiantes()
            doc = input("Ingrese numero de documento del estudiante:  ")
            for estudiante in estudiantes:
                if  doc in estudiante:
                    op = int(input("Desea Elimnar a un camper del sistemal? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        estudiante.pop(doc)
                        print(f"Estudiante con documento {doc} ha sido Eliminado")
                        guardar_datos_Estudiantes(estudiantes)
                        return
                    elif op == 2:
                        
                        return
                    else:
                        print("Opción no válida.")
                        return
                
            print("Estudiante no registrado.")
            return#aparece por que si    
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
    
def asigancion_trasiner_camper ():
    while True:
        try:
            estudiantes = cargar_datos_estudiantes()
            doc = input("Ingrese numero de documento del estudiante:  ")
            for estudiante in estudiantes:
                if  doc in estudiante:
                    op = int(input("Desea agregar un trainner ? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        estudiante[doc]["Profesor"]=input("Ingrese el nombre del trainer")
                        print("Trainer asigando exitosamente")
                        guardar_datos_Estudiantes(estudiantes)
                        return
                    elif op == 2:
                        return
                    else:
                        print("Opción no válida.")
                        return
                
            print("Estudiante no registrado.")
            return  
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
            
def asigancion_Ruta_camper ():
    while True:
        try:
            estudiantes = cargar_datos_estudiantes()
            doc = input("Ingrese numero de documento del estudiante:  ")
            for estudiante in estudiantes:
                if  doc in estudiante:
                    op = int(input("Desea agregar una ruta ? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        
                        estudiante[doc]["Ruta"]=input("Ingrese el nombre de la Ruta")
                        print("Ruta asiganda exitosamente")
                        guardar_datos_Estudiantes(estudiantes)
                        return
                    elif op == 2:
                        return
                    else:
                        print("Opción no válida.")
                        return
                
            print("Estudiante no registrado.") 
            return     
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")  
        

def cambiar_riesgo_camper_Alto():
    while True:
        try:
            estudiantes = cargar_datos_estudiantes()
            for estudiante in estudiantes:
                for llave, valor in estudiante.items():
                    if estudiante[llave]["Riesgo"]=="Riesgo Alto":
                        print (f"Estudiante con documento {llave}  y nombre {estudiante[llave]['Nombre']} esta en Riesgo")
                    #imprimir la listae campers
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
#Registro_de_estudiantes()
#listar_campers()
#cambiar_estado_camper()
#cambiar_riesgo_camper_Alto()
#consultar_Camper()
#cambiar_infopersonal_camper()
#Eliminar_camper()
#asigancion_trasiner_camper()
#
         