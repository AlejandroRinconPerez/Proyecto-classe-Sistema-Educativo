from turtle import update
from F_Datos_Rutas import*
from D_Datos_Trainners import*
from D_Registro_Trainers import*
from B_Datos_Candidatos import*
from B_Registro_candidatos import*
from C_Registro_Estudiantes import*
from C_Datos_Estudiantes import*

def salon_Hotario ():
    while True:
        try:
                print(' Seleccione el Horario deseado')
                Horarios = ["1. Horario 6-10 spuknik",
                            "2. Horario 10-14 spuknik",
                            "3. Horario 14-18 spuknik" ,
                            "4.Horario 18-22 spuknik",
                            "5. Horario 6-10 Apolo",
                            "6. Horario 10-14 Apolo",
                            "7. Horario 14-18 Apolo" ,
                            "8. Horario 18-22 Apolo",
                            "9. Horario 6-10 Artemis",
                            "10. Horario 10-14 Artemis",
                            "11. Horario 14-18 Artemis" ,
                            "12. Horario 18-22 Artemis",
                            "13. salir"]
                for i in Horarios:
                    print(i)
                ruta = {}
                op = int(input(" Ingrese el horario que quiere "))
                if op == 1:
                    return  "Horario 6-10 spuknik"
                elif op == 2:
                    return "Horario 10-14 spuknik"
                elif op == 3:
                    return  "Horario 14-18 spuknik"
                elif op == 4:
                    return  "Horario 18-22 spuknik"
                elif op == 5:
                    return  "Horario 6-10 Apolo"
                elif op == 6:
                    return  "Horario 10-14 Apolo"
                elif op == 7:
                    return  "Horario 14-18 Apolo"
                elif op == 8:
                    return  "Horario 18-20 Apolo"
                elif op == 9:
                    return  "Horario 6-10 Artemis"
                elif op == 10:
                    return  "Horario 10-14 Artemis"
                elif op == 11:
                    return  "Horario 14-18 Artemis"
                elif op == 12:
                    return  "Horario 18-20 Artemis"
                elif op == 13:
                    return 
                else:
                    print("Opcion no valida Apolo" )    
                return 
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
def Horarios_Salon_rutas ():
    while True:
        try:
            rutas = cargar_datos_rutas()
            hora = salon_Hotario ()
            print(hora)
            for ruta in rutas:
                    if hora in ruta:
                        print( "Horario ya existe y esta asignado")
                        op2 = input("Desea continuar y sobre escribir el horario 1. SI  2. NO?")
                        if op2 == 2:
                            return
            ruta = {hora: {}}
            rutas.append(ruta)
            print("---------------------------------------")
            print("Ahora vamos a asignar ese horario a un grupo")
            Nombre_Grupo = input (" Ingrese el nombre del Gurpo:  ")
            ruta[hora][Nombre_Grupo]={}
            print("---------------------------------------")
            print("Ahora vamos a asignar una ruta")
            print( " Aca puedes elegir un nombre de ruta o asignarle nombre")
            print(" los existentes son: Ruta NodeJS, Ruta Java  y   Ruta NetCore")
            Nombre_Ruta = input(" Nombre la nueva ruta")
            ruta[hora][Nombre_Grupo][Nombre_Ruta]={}
            guardar_datos_rutas(rutas)
            Modulos ={}
            print("---------------------------------------")
            print("Escriba el nombre de los modulos que debe llevar" )
            print("Las opcioners son: nota: Puede escribir las 2 rutas")

            print("ParaFundamentos de programacion  ")
            Modulos["Fundamentos de programacioon"] = input("Introducción a la algoritmia - PSeInt - Python:  ")
            
            print("Programacion Web")
            Modulos["Programacion Web"] = input("HTML - CSS - Bootstrap:")
            
            print("Programación formal")
            Modulos["Programacioon formal"] = input("Java - JavaScript - C#: ")
            
            print("Bases de datos")
            Modulos["Bases de datos"] = input("Mysql - MongoDb - Postgresql ")
            
            print("Backend ")
            Modulos["Backend"] = input("NetCore - Spring Boot - NodeJS - Express  ")
            
        
            ruta[hora][Nombre_Grupo][Nombre_Ruta] =Modulos
            
            print("-------------------------")
            guardar_datos_rutas(rutas)
            return 
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
    

            
def agregar_estudiante_ruta():
    while True:
        try:
            rutas = cargar_datos_rutas()
            estudiantes = cargar_datos_estudiantes()
            hora = salon_Hotario ()
            Nombre_Grupo = input("Ingrese grupo, ej. U2, U1, A2: ")
            cantidad = int(input("¿Cuántos estudiantes desea ingresar? "))

            for ruta in rutas:
                if hora in ruta and Nombre_Grupo in ruta[hora]:
                    if "Aula" not in ruta[hora][Nombre_Grupo]:
                        ruta[hora][Nombre_Grupo]["Aula"] = {}

                    estudiantes_actuales = len(ruta[hora][Nombre_Grupo]["Aula"])
                    if estudiantes_actuales + cantidad > 33:
                        print(f"No se pueden agregar {cantidad} estudiantes. El límite es 33 y ya hay {estudiantes_actuales} estudiantes en el aula.")
                        return
                    
                    for i in range(cantidad):
                        doc = input("Ingrese documento: ")
                        for estudiante in estudiantes:
                            if doc in estudiante:
                                ruta[hora][Nombre_Grupo]["Aula"][doc] = estudiante[doc]
                    guardar_datos_rutas(rutas)
                    print("Datos guardados exitosamente!")
                    return
            print("No se encontró el horario o el grupo especificado.")
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
    
        
def agregar_Profesor_ruta():
    while True:
        try:
            rutas = cargar_datos_rutas()
            Trainers = cargar_datos_trainers()
            hora = salon_Hotario ()
            Nombre_Grupo = input("Ingrese grupo, ej. U2, U1, A2: ")
            for ruta in rutas:
                if hora in ruta and Nombre_Grupo in ruta[hora]:
                    if "Profe" not in ruta[hora][Nombre_Grupo]:
                        ruta[hora][Nombre_Grupo]["Profe"] = {}   
                        
                    doc = input("Ingrese documento: ")
                    for trainer in Trainers:
                        if doc in trainer:
                            ruta[hora][Nombre_Grupo]["Profe"][doc] = trainer[doc]
                    guardar_datos_rutas(rutas)
                    print("Datos guardados exitosamente!")
                    return
            
            print("No se encontró el horario o el grupo especificado.")
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
        
        
def ver_Camper_por_Ruta_con_Profe():
    while True:
        try:
            rutas = cargar_datos_rutas()
            for ruta in rutas:
                for hora, grupo_datos in ruta.items():
                    for grupo, datos_grupo in grupo_datos.items():
                        if "Aula" in list(datos_grupo.keys()):
                            print(f"Grupo: {grupo}")
                            for doc, estudiante in datos_grupo["Aula"].items():
                                print(f"En el Horario  {hora}")
                                print(f"Estudiante ID: {doc}")
                                print(f"Nombre: {estudiante['Nombre']}")
                                print(f"Apellido: {estudiante['Apellido']}")
                                
                        elif "Profe" in datos_grupo:
                            print(f"Grupo: {grupo}")
                            for docp, profe_info in datos_grupo["Profe"].items():
                                print(f"En el Horario  {hora}")
                                print(f"Profesor ID: {docp}")
                                print(f"Nombre: {profe_info['Nombre']}")
                                print(f"Apellido: {profe_info['Apellido']}")
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
        
            
def camper_ruta ():     
    while True:
        try:
            rutas = cargar_datos_rutas()
            for ruta in rutas:
                for hora, grupo_datos in ruta.items():
                    for grupo, datos_grupo in grupo_datos.items():
                        if "Aula" in datos_grupo:
                            print(f"Grupo: {grupo}")
                            for doc, estudiante in datos_grupo["Aula"].items():
                                
                                print(f"En el Horario  {hora}")
                                print(f"Estudiante ID: {doc}")
                                print(f"Nombre: {estudiante['Nombre']}")
                                print(f"Apellido: {estudiante['Apellido']}")
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
            
def camper_ruta_solo ():  
    while True:
        try:
            doc2 = input("Ingrese su docuemnto") 
            rutas = cargar_datos_rutas()
            for ruta in rutas:
                for hora, grupo_datos in ruta.items():
                    for grupo, datos_grupo in grupo_datos.items():
                        if "Aula" in datos_grupo:
                            print(f"Grupo: {grupo}")
                            for doc, estudiante in datos_grupo["Aula"].items():
                                if doc == doc2:
                                    print(f"En el Horario  {hora}")
                                    print(f"Estudiante ID: {doc}")
                                    print(f"Nombre: {estudiante['Nombre']}")
                                    print(f"Apellido: {estudiante['Apellido']}")
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
def Profe_Ruta():
    while True:
        try:
            rutas = cargar_datos_rutas()
            for ruta in rutas:
                for hora, grupo_datos in ruta.items():
                    for grupo, datos_grupo in grupo_datos.items():
                        if "Profe" in datos_grupo:
                            print(f"Grupo: {grupo}")
                            for profe_id, profe_info in datos_grupo["Profe"].items():
                                print(f"En el Horario  {hora}")
                                print(f"Profesor ID: {profe_id}")
                                print(f"Nombre: {profe_info['Nombre']}")
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")    



    

    
    
    

    
    
    
    
    
    
    
    
    

    
    
    
   
    
    
    
        


