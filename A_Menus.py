from Z_Datos import*
from B_Registro_candidatos import*
from C_Registro_Estudiantes import*
from D_Registro_Trainers import*
from E_Registro_Notas import*
from F_Registro_Rutas import*
from F_Datos_Rutas import *

def Mostrar_menu_principal():
    while True:
        try:
            print("-------------------------------------------------------")
            opciones_principal = ["1. Para coordinador", 
                                "2. Para Trainer", 
                                "3. Para estudiante",
                                "4. Para ver los Reportes",
                                "5. Para  Rutas",
                                "6. Para salir"]
            for i in opciones_principal:
                print(i)
            op_Principal = int(input("Ingrese la opción de menú deseado: "))
            print("-------------------------------------------------------")
            return op_Principal
        except Exception as e:
                print(f"Se ha producido un error: {e}")
                print("Por favor, intente nuevamente.")
def Mostrar_menu_coordinador():
    while True:
        try:
            print("-------------------------------------------------------")
            opciones_coordinador = ["1. Para inscritos",
                                    "2. Para Trainer", 
                                    "3. Para Camper",
                                    "4. Para salir"]
                                    
            for i in opciones_coordinador:
                print(i)
            op_cordinador = int(input("Ingrese la opción de menú deseado: "))
            print("-------------------------------------------------------")
            return op_cordinador
        except Exception as e:
                print(f"Se ha producido un error: {e}")
                print("Por favor, intente nuevamente.")

def menu_Camper():
    while True:
        try:
            print("-------------------------------------------------------")
            opciones_camper = ["1. Para ver notas",
                                    "2. Para ver horario", 
                                    "3. Para salir"]
            for i in opciones_camper :
                print(i)
            opciones_camper2 = int(input("Ingrese la opción de menú deseado: "))
            print("-------------------------------------------------------")
            return opciones_camper2
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
            
def Mostrar_cordinador_incritos():
    while True:
        try:
            print("-------------------------------------------------------")
            opciones_coordinador_inscritos = ["1. Para Ingresar un Camper ",
                                            "2. Para agregar notas examen practico y teorico",
                                            "3. Para salir"]
            for i in opciones_coordinador_inscritos:
                print(i)
            op_inscritos = int(input("Ingrese la opción de menú deseado: "))
            print("-------------------------------------------------------")
            return op_inscritos
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")

def Mostrar_coordinador_campers():
    while True:
        try:
            opciones_coordinador_Campers = ["1. Para Registrar Camper ",
                                            "2. Para Ver Datos de todos camper",
                                            "3. Para Cambiar estado de un camper",
                                            "4. Para ver un solo Camper",
                                            "5. Para Cambiar informacion personal de un camper",
                                            "6. Para Eliminar un camper",
                                            "7. Para Asignar profesor a un Camper",
                                            "8. Para Asignarle una ruta al Camper",
                                            "9. Para Cambiar o agregar notas de un camper cursando", # modulo notas
                                            "10. Para ver notas de un camper",
                                            "11. Para Salir"]
            for i in opciones_coordinador_Campers:
                print(i)
            op_Campers = int(input("Ingrese la opción de menú deseado: "))
            print("-------------------------------------------------------")
            return op_Campers
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")

def Mostrar_coordinador_trainers():
    while True:
        try:
            opciones_coordinador_trainers = ["1. Para Registro de trainers",
                                            "2. Para Consultar un trainer",
                                            "3. Para Cambiar informacion personal de un trainer",
                                            "4. Para Eliminar a un trainer",
                                            "5. Para ver el listado de todos los trainers",
                                            "6. Para asignarle una ruta a un trainer",
                                            "7. Para ver la ruta de un trainer",
                                            "8. Para Salir"]
            
            for i in opciones_coordinador_trainers:
                print(i)
            op_Trainsers = int(input("Ingrese la opción de menú deseado: "))
            print("-------------------------------------------------------")
            return op_Trainsers
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")

def Trainer_menu():
    while True:
        try:
            opciones_trainner = ["1. Para ver ver horario id nombre", # def trainer_ruta ():
                                "2. Para asignar notas en un modulo(n)",
                                "3. Para Ver las notas de un camper",
                                "4. Para salir"]
            for i in opciones_trainner:
                print(i)
            op_trainers2 = int(input("Ingrese la opción de menú deseado: "))
            print("-------------------------------------------------------")
            return op_trainers2
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")

def sub_menu_reportes():
    while True:
        try:
            print("-------------------------------------------------------")
            menu_sub_reportes = ["1. Listar los campers que se encuentren en estado de inscrito",
                                "2. Listar los campers que aprobaron el examen inicial", 
                                "3. Listar los entrenadores que se encuentran trabajando con CampusLands",
                                "4. Listar los campers que no están aprobados",
                                "5. Listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento",
                                "6. Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado", 
                                "7. Para salir"]
            for i in menu_sub_reportes:
                print(i)
            op_Reportes = int(input("Ingrese la opción de menú deseado: "))
            print("-------------------------------------------------------")
            return op_Reportes
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
def Menu_ruta():
    while True:
        try:
            print("-------------------------------------------------------")
            menu_rutaa = ["1. Agregar Ruta", #Horarios_Salon_rutas ()
                                "2. Agregar estudiantes a una ruta", #agregar_estudiante_ruta()
                                "3. Agregar un profesor a un aula",#agregar_Profesor_ruta()
                                "4. Ver relacion Camper, Ruta y trannier",#()
                                "5. Relacion camper ruta",  #camper_ruta_solo ()
                                "6. Para salir"]
            for i in menu_rutaa:
                print(i)
            op_Ruta = int(input("Ingrese la opción de menú deseado: "))
            print("-------------------------------------------------------")
            return op_Ruta
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            

while True: 
    op_Principal = Mostrar_menu_principal()
    if op_Principal == 1:
        op_cordinador = Mostrar_menu_coordinador()
        if op_cordinador == 1:
            op_inscritos = Mostrar_cordinador_incritos()
            if op_inscritos == 1:
                Registro_de_candidatos()
            elif op_inscritos == 2:
                Registro_Notas_Candidatos()
            elif op_inscritos == 3:
                print("Volviendo al Menu")
            else:
                print("Opción no válida")
        elif op_cordinador == 2:
            op_Trainsers = Mostrar_coordinador_trainers()
            if op_Trainsers == 1:
                Registro_de_trainers()
            elif op_Trainsers == 2:
                Profe_Ruta()
            elif op_Trainsers == 3:
                cambiar_infoperonal_trainer()
            elif op_Trainsers == 4:
                eliminar_trainer()
            elif op_Trainsers == 5:
                Profe_Ruta()
            elif op_Trainsers == 6:
                agregar_Profesor_ruta() 
            elif op_Trainsers == 7:
                Profe_Ruta()
            elif op_Trainsers == 8:
                print("Volviendo al Menu")
                
            else:
                print("Opción no válida")
        elif op_cordinador == 3:
            op_Campers = Mostrar_coordinador_campers()
            if op_Campers == 1:
                Registro_de_estudiantes()
            elif op_Campers == 2:
                camper_ruta()
            elif op_Campers == 3:
                cambiar_estado_camper()
            elif op_Campers == 4:
                consultar_Camper()
            elif op_Campers == 5:
                cambiar_infopersonal_camper()
            elif op_Campers == 6:
                Eliminar_camper()
            elif op_Campers == 7:
                agregar_Profesor_ruta()
            elif op_Campers == 8:
                agregar_estudiante_ruta()
            elif op_Campers == 9:
                Registro_moduloXX()
            elif op_Campers == 10:
                Mostrar_Notas_Estudiante()
            elif op_Campers == 11:
                print("Volviendo al Menu")
                
            else:
                print("Opción no válida")
    elif op_Principal == 2:
        op_trainers2 = Trainer_menu()
        if op_trainers2 == 1:
            Profe_Ruta()
        elif op_trainers2 == 2:
            Registro_moduloXX()
        elif op_trainers2 == 3:
            Mostrar_Notas_Estudiante()
        elif op_trainers2 == 4:
            print("Volviendo al Menu")
            
    elif op_Principal == 3:
        opciones_camper2 = menu_Camper()
        if opciones_camper2 == 1:
             Mostrar_Notas_Estudiante()
        elif opciones_camper2 == 2:
            camper_ruta_solo()
        elif opciones_camper2 == 3:
            print("Volviendo al Menu")
            
    elif op_Principal == 4:
        op_Reportes = sub_menu_reportes()
        if op_Reportes == 1:
            ver_inscritos()
        elif op_Reportes == 2:
            Ver_Candidatos_Aprobados()
        elif op_Reportes == 3:
            Profe_Ruta()
        elif op_Reportes == 4:
            cambiar_riesgo_camper_Alto()
        elif op_Reportes == 5:
            ver_Camper_por_Ruta_con_Profe()
        elif op_Reportes == 6:
            Profe_Ruta()
            ver_Camper_por_Ruta_con_Profe()
            print("No realizado") # Falta asociar las rutas y notas
        elif op_Reportes == 7:
            print("Volviendo al Menu")
            
    elif op_Principal == 5:
        op_Ruta =  Menu_ruta()
        if op_Ruta == 1:
            Horarios_Salon_rutas ()
        elif op_Ruta == 2:
            agregar_estudiante_ruta()
        elif op_Ruta == 3:
            agregar_Profesor_ruta()
        elif op_Ruta == 4:
            ver_Camper_por_Ruta_con_Profe()
        elif op_Ruta == 5:
            camper_ruta_solo ()
        elif op_Ruta == 6:
            print("Volviendo al Menu")
        
    elif op_Principal == 6:
        break
    
    
    
    
    
    
    
