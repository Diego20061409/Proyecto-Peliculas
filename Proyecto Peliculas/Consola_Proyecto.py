import Modulo_Proyecto as mod

peli1 = {"nombre": "Shrek", "genero": "Familiar, Comedia", "duracion": 92, "anio": 2001, "clasificacion": 'Todos', "hora": 1700, "dia": "Viernes"}
peli2 = {"nombre": "Get Out", "genero": "Suspenso, Terror", "duracion": 104, "anio": 2017, "clasificacion": '18+', "hora": 2330, "dia": "Sábado"}
peli3 = {"nombre": "Icarus", "genero": "Documental, Suspenso", "duracion": 122, "anio": 2017, "clasificacion": '18+', "hora": 800, "dia": "Domingo"}
peli4 = {"nombre": "Inception", "genero": "Acción, Drama", "duracion": 148, "anio": 2010, "clasificacion": '13+', "hora": 1300, "dia": "Lunes"}
peli5 = {"nombre": "The Empire Strikes Back", "genero": "Familiar, Ciencia-Ficción", "duracion": 124, "anio": 1980, "clasificacion": '7+', "hora": 1415, "dia": "Miércoles"}

peliculas = [peli1, peli2, peli3, peli4, peli5]

def mostrar_informacion_pelicula(pelicula: dict) -> None:
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Año: " + str(anio) + " - Duración: " + str(duracion) + " mins")
    print("Género: " + genero + " - Clasificación: " + clasificacion)

    hora_formato = f"{hora // 100:02}:{hora % 100:02}"
    print("Día: " + dia + " Hora: " + hora_formato)

def ejecutar_encontrar_pelicula_mas_larga(peli1: dict, peli2: dict, peli3: dict, peli4: dict, peli5: dict) -> None:
    """Ejecuta la búsqueda de la película más larga y muestra el resultado."""
    peliculas = [peli1, peli2, peli3, peli4, peli5]
    pelicula_mas_larga = mod.encontrar_pelicula_mas_larga(peliculas)
    print(f"La película más larga es: {pelicula_mas_larga['nombre']} - Duración: {pelicula_mas_larga['duracion']} mins")

def ejecutar_consultar_duracion_promedio_peliculas(peli1: dict, peli2: dict, peli3: dict, peli4: dict, peli5: dict) -> None:
    duracion_promedio = mod.duracion_promedio_peliculas(peli1, peli2, peli3, peli4, peli5)
    print(duracion_promedio)
     
def ejecutar_encontrar_estrenos(peli1: dict, peli2: dict, peli3: dict, peli4: dict, peli5: dict) -> None:
    anio = int(input("Ingrese el año a partir del cual desea buscar estrenos: "))
    estrenos = mod.encontrar_estrenos(peli1, peli2, peli3, peli4, peli5, anio)
    print(f"Estrenos a partir del año {anio}: {estrenos}")

def ejecutar_cuantas_peliculas_18_mas(peli1: dict, peli2: dict, peli3: dict, peli4: dict, peli5: dict) -> None:
    cantidad = mod.cuantas_peliculas_18_mas(peli1, peli2, peli3, peli4, peli5)
    print(f"Cantidad de películas con clasificación 18+: {cantidad}")

def ejecutar_reagendar_pelicula(peliculas: list) -> None:
    """Ejecuta la opción de reagendar una película."""
    
    print("Reagendar una película de la agenda")

    nombre = input("Ingrese el nombre de la película que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre, *peliculas)
    
    if pelicula is None:
        print("No hay ninguna película con este nombre.")
    else:
        nueva_hora = input('Ingresa nueva hora: ')
        while True:
            if len(nueva_hora) != 4 or not nueva_hora.isdigit():
                print("Hora inválida.")
                nueva_hora = input('Ingresa nueva hora: ')
                continue
            
            hora = int(nueva_hora[:2])
            minutos = int(nueva_hora[2:])
            
            if (hora < 0 or hora > 23) or (minutos < 0 or minutos >= 60):
                print("Hora inválida. ")
                nueva_hora = input('Ingresa nueva hora: ')
            else:
                break
        
        nuevo_dia = input('Ingrese nuevo día: ')
        control_horario = input("¿Desea controlar el horario de la película? (si/no): ").strip().lower() == 'si'
        resultado = mod.reagendar_pelicula(pelicula, int(nueva_hora), nuevo_dia, control_horario, *peliculas)
        
        if resultado:
            pelicula["hora"] = int(nueva_hora)
            pelicula["dia"] = nuevo_dia
            print(f"La película '{pelicula['nombre']}' ha sido reagendada a las {nueva_hora} el día {nuevo_dia}.")
        else:
            print(f"No se pudo reagendar la película '{pelicula['nombre']}' debido a conflictos de horario o restricciones de género.")


def ejecutar_decidir_invitar(peli1: dict, peli2: dict, peli3: dict, peli4: dict, peli5: dict) -> None:
    print("Decidir si se puede invitar a alguien a ver una película")

    nom_peli = input("Ingrese el nombre de la película: ")
    pelicula = mod.encontrar_pelicula(nom_peli, peli1, peli2, peli3, peli4, peli5)

    if pelicula is None:
        print("No hay ninguna película con este nombre.")
    else:
        edad_invitado = int(input("Ingrese la edad del invitado: "))
        autorizacion_padres = input("¿Tiene autorización de los padres? (si/no): ").strip().lower() == 'si'

        puede_invitar = mod.decidir_invitar(pelicula, edad_invitado, autorizacion_padres)

        if puede_invitar:
            print("Puedes invitar a esta persona a ver la película.")
        else:
            print("No puedes invitar a esta persona a ver la película.")

def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola.
    Esta funcion primero crea las cinco peliculas que se van a manejar en la agenda.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    pelicula1 = mod.crear_pelicula("Shrek",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
    pelicula2 = mod.crear_pelicula("Get Out",  "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")  
    pelicula3 = mod.crear_pelicula("Icarus",  "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
    pelicula4 = mod.crear_pelicula("Inception",  "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
    pelicula5 = mod.crear_pelicula("The Empire Strikes Back",  "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")   
    
    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de peliculas para la semana de receso" +"\n"+("-"*50))
        print("Pelicula 1")
        mostrar_informacion_pelicula(peli1)
        print("-"*50)
        
        print("Pelicula 2")
        mostrar_informacion_pelicula(peli2)
        print("-"*50)
        
        print("Pelicula 3")
        mostrar_informacion_pelicula(peli3)
        print("-"*50)
        
        print("Pelicula 4")
        mostrar_informacion_pelicula(peli4)
        print("-"*50)
        
        print("Pelicula 5")
        mostrar_informacion_pelicula(peli5)
        print("-"*50)
        
        ejecutando = mostrar_menu_aplicacion(peli1, peli2, peli3, peli4, peli5)
        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")
        
def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4:dict, p5:dict) -> bool:
    """Le muestra al usuario las opciones de ejecución disponibles.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente 
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opción para salir 
        de la aplicacion.
    """
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")    
    print(" 7 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(*peliculas)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(peli1, peli2, peli3, peli4, peli5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(peli1, peli2, peli3, peli4, peli5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(peli1, peli2, peli3, peli4, peli5)        
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(peliculas) 
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(peli1, peli2, peli3, peli4, peli5) 
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando


iniciar_aplicacion()

