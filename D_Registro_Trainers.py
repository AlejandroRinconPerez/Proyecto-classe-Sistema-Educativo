from D_Datos_Trainners import*


def Registro_de_trainers():
    while True:
        try:
            Trainers = cargar_datos_trainers()
            doc = input("Ingrese numero de documento del Trainer:  ")
            for trainer in Trainers:
                if trainer.get(doc,None) != None:
                    # candidatos[i][doc]["estado"]=nuevo
                    print("Trainer ha sido registrado anteriormente")
                    return
            Personales_trainer = {}
            Personales_trainer["Nombre"] = input("Ingrese el nombre:  ")
            Personales_trainer["Apellido"] = input("Ingrese el Apellido:  ")
            Personales_trainer["Telefono"] = input("Ingrese el Telefono:  ")
            doc_estudiante = None
            estudiantes = [doc_estudiante] 
            Personales_trainer["Estudiantes"]=estudiantes
            trainer = {}
            trainer[doc]=Personales_trainer
            Trainers.append(trainer)
            guardar_datos_Trainers(Trainers)
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
                
def Consultar_trainers():
    while True:
        try:
            Trainers = cargar_datos_trainers()
            doc = input("Ingrese numero de documento del Trainer:  ")
            for trainer in Trainers:
                if doc in trainer:
                    for llave, valor in trainer.items():
                        print(llave, valor)
                        return
                
            print("Trainer no Registrado")
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
def cambiar_infoperonal_trainer ():
    while True:
        try:
            Trainers = cargar_datos_trainers()
            doc = input("Ingrese numero de documento del Trainer:  ")
            for trainer in Trainers:
                if doc in trainer:
                    op = int(input("Desea cambiar la informacion personal? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        trainer[doc]["Nombre"]=input("Actualice el nombre:  ")
                        trainer[doc]["Apellido"] = input("Actualice el Apellido:  ")
                        trainer[doc]["Telefono"] = input("Actualice el Telefono:  ")
                        trainer[doc]["Cantidad de Horarios"] =input("Ingrese la cantidad de horarios Nueva:  ")
                        print("Estado actualizado correctamente.")
                        guardar_datos_Trainers(Trainers)
                        return
                    elif op == 2:
                        return
                    else:
                        print("Opción no válida.")
                        return
                
            print("Trainer no registrado.")
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
    
def eliminar_trainer():
    while True:
        try:
            Trainers = cargar_datos_trainers()
            doc = input("Ingrese numero de documento del Trainer:  ")
            for trainer in Trainers:
                if doc in trainer:
                    op = int(input("Desea Eliminar el trainer? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        trainer.pop(doc)
                        print(f"Trainer con documento {doc} ha sido Eliminado")
                        guardar_datos_Trainers(Trainers)
                        return
                    elif op == 2:
                        return
                    else:
                        print("Opción no válida.")
                        return
                
            print("Trainer no registrado.")
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
    
def lista_trainers ():
    while True:
        try:
            Trainers = cargar_datos_trainers()
            cont = 0
            for trainer in Trainers:
                for llave, valor in trainer.items():
                    cont = cont + 1
                    print(f"El trainer {trainer[llave]["Nombre"]} con las rutas  {trainer[llave]["Rutas"]}")
                    
            return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
                
def asignar_rutas_trainer ():
    while True:
        try:
            Trainers = cargar_datos_trainers()
            doc = input("Ingrese numero de documento del Trainer:  ")
            cantidad = int(input("Cauntas rutras desea asignar"))
            for trainer in Trainers:
                if doc in trainer:
                    op = int(input("Desea asignar las Rutas al trainer? 1. Para SI 2. Para NO: "))
                    if op == 1:
                        trainer[doc]["Rutas"].clear()
                        for i in range(cantidad):
                            if trainer[doc]["Rutas"] is None:
                                trainer[doc]["Rutas"] = []
                            Nueva_ruta=input("Ingrese las rutas:  ")
                            trainer[doc]["Rutas"].append(Nueva_ruta)
                        print("Estado actualizado correctamente.")
                        guardar_datos_Trainers(Trainers)
                        return
                    elif op == 2:
                        return
                    else:
                        print("Opción no válida.")
                        return
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
def trainer_ruta ():

            Trainers = cargar_datos_trainers()
            for trainer in Trainers:
                for  llave, valor in trainer.items(): 
                    print(f"El trainer {valor['Nombre']} tiene asignado: {valor['Rutas']}")
            return
        
    
#trainer_ruta ()
                   

    #554390
#Registro_de_trainers()
#Consultar_trainers()
#cambiar_infoperonal_trainer (
#eliminar_trainer()
#lista_trainers()
#asignar_rutas_trainer()
#trainer_ruta()
#lista_trainers ()

