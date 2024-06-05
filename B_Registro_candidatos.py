from B_Datos_Candidatos import*


def Registro_de_candidatos():
    while True:
        try:
            candidatos = cargar_datos_candidatos()
            doc = input("Ingrese numero de documento del candidato:  ")
            for candidato in candidatos:
                if candidato.get(doc,None) != None:
                    print("Candidato ha sido registrado anteriormente")
                    return
            Personales_Candidato = {}
            Personales_Candidato["Nombre"] = input("Ingrese el nombre:  ")
            Personales_Candidato["Apellido"] = input("Ingrese el Apellido:  ")
            
            Personales_Candidato["Telefono"] = int(input("Ingrese el Telefono:  "))
            Personales_Candidato["Nota examen Teorico"] = False
            Personales_Candidato["Nota examen practico"] = False
            Personales_Candidato["Aprobado"]= None
            candidato = {}
            candidato[doc]=Personales_Candidato
            #agreaggr el horario a la info personal
            candidatos.append(candidato)
            guardar_datos_Candidatos(candidatos)
            break
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
def Registro_Notas_Candidatos():
    while True:
        try:
            candidatos = cargar_datos_candidatos()
            doc = input("Ingrese numero de documento del candidato:  ")
            for candidato in candidatos:
                if doc in candidato:
                    candidato[doc]["Nota examen Teorico"] = int(input("Ingrese la nota del examen Teorico:  "))#possible error 
                    candidato[doc]["Nota examen practico"] = int(input("Ingrese la nota del eamen practico:   "))
                    x = (candidato[doc]["Nota examen practico"] + candidato[doc]["Nota examen Teorico"]) / 2
                    candidato[doc]["Aprobado"] = x > 59
                    print("Estado actualizado correctamente.")
                    guardar_datos_Candidatos(candidatos) 
                    return
                
            print("No inscrito")
            break
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
def Ver_Candidatos():
    while True:
        try:
    
            candidatos = cargar_datos_candidatos()
            doc = input("Ingrese numero de documento del camper inscrito:  ")
            for candidato in candidatos:
                if doc in candidato :
                    print(f"Estudiante inscrito {candidato[doc]}")
                    return
                
            print("No inscrito")
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            break
def Ver_Candidatos_Aprobados():
    while True:
        try:
            candidatos = cargar_datos_candidatos()
            for candidato in candidatos:
                for llave, valor in candidato.items():
                    if candidato[llave]["Aprobado"] == True:
                        print(f"Este camper {candidato[llave]["Nombre"]}aprobo el examen inicial # doc ={llave}")
                        return
            print("No inscrito o no aprobo")
            break
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
def ver_inscritos ():
    while True:
        try:
            candidatos = cargar_datos_candidatos()
            for candidato in candidatos:
                for llave, valor in candidato.items():
                    print( f" Nombre de cmper inscrito {candidato[llave]["Nombre"]} con documento {llave}")
            break
        except Exception as e:
            print(f"Se ha producido un error: {e}")
            print("Por favor, intente nuevamente.")
            
    

        
    
    
    
    
    
#Registro_de_candidatos()
#Registro_Notas_Candidatos()
#Ver_Candidatos()  
#Ver_Candidatos_Aprobados()   
#Ver_Candidatos_Aprobados() 
#Ver_Candidatos()
#ver_inscritos()