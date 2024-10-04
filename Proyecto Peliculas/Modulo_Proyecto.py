def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, clasificacion: str, hora: int, dia: str) -> dict:
    return {
        'nombre': nombre,
        'genero': genero,
        'duracion': duracion,
        'anio': anio,
        'clasificacion': clasificacion,
        'hora': hora,
        'dia': dia
    }

peli1 = crear_pelicula("Shrek",  "Familiar, Comedia", 92, 2001, 'todos', 1700, "Viernes")
peli2 = crear_pelicula("Get Out",  "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")
peli3 = crear_pelicula("Icarus",  "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
peli4 = crear_pelicula("Inception",  "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
peli5 = crear_pelicula("The Empire Strikes Back",  "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")

peliculas = [peli1, peli2, peli3, peli4, peli5]

d={peli1['nombre']:peli1, peli2['nombre']:peli2, peli3['nombre']:peli3, peli4['nombre']:peli4, peli5['nombre']:peli5 }

print(d["Get Out"])
print(d["Shrek"])
print(d["Icarus"])
print(d["Inception"])
print(d["The Empire Strikes Back"])

def encontrar_pelicula(nombre_pelicula: str, peli1: dict, peli2: dict, peli3: dict, peli4: dict,  peli5: dict) -> dict:

    d={peli1['nombre']:peli1, peli2['nombre']:peli2, peli3['nombre']:peli3, peli4['nombre']:peli4, peli5['nombre']:peli5}
    if nombre_pelicula not in d:
        return None

    return d[nombre_pelicula]
print(encontrar_pelicula("Shrek", peli1, peli2, peli3, peli4, peli5))

def encontrar_pelicula_mas_larga(peliculas: list) -> dict:
    l = [pelicula['duracion'] for pelicula in peliculas]
    for pelicula in peliculas:
        if pelicula['duracion'] == max(l):
            return pelicula
print(f"La película más larga es: {encontrar_pelicula_mas_larga(peliculas)['nombre']} - Duración: {encontrar_pelicula_mas_larga(peliculas)['duracion']} mins")

def duracion_promedio_peliculas(peli1: dict, peli2: dict, peli3: dict, peli4: dict, peli5: dict) -> str:
    total_duracion = peli1['duracion'] + peli2['duracion'] + peli3['duracion'] + peli4['duracion'] + peli5['duracion']
    
    duracion_promedio = total_duracion / 5
    
    horas = int(duracion_promedio // 60)
    minutos = int(duracion_promedio % 60)
    
    return f"{horas}:{minutos:02d}"

print(duracion_promedio_peliculas(peli1, peli2, peli3, peli4, peli5))

def encontrar_estrenos(peli1: dict, peli2: dict, peli3: dict, peli4: dict, peli5: dict, anio: int) -> str:
    l=[peli1['anio'], peli2['anio'], peli3['anio'], peli4['anio'], peli5['anio']]
    peliculas = [peli1,peli2,peli3,peli4,peli5]
    nombres = []
    for pelicula in peliculas:
        if pelicula['anio'] >= anio:
            nombres.append(pelicula['nombre'])
    return ', '.join(nombres) if nombres else 'No hay estrenos'
print(encontrar_estrenos(peli1, peli2, peli3, peli4, peli5, 2010))

def cuantas_peliculas_18_mas(peli1: dict, peli2: dict, peli3: dict, peli4: dict, peli5: dict) -> int:
    peliculas = [peli1, peli2, peli3, peli4, peli5]
    cont = 0
    for pelicula in peliculas:
        if pelicula['clasificacion'] == '18+':
            cont += 1
    return cont
print(cuantas_peliculas_18_mas(peli1, peli2, peli3, peli4, peli5))

def reagendar_pelicula(peli: dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    duracion_peli = peli["duracion"]
    nueva_hora_fin = nueva_hora + (duracion_peli // 100) * 60 + (duracion_peli % 100)
    peliculas = [p1, p2, p3, p4, p5]
    for p in peliculas:
        if p != peli and p["dia"] == nuevo_dia:
            hora_fin = p["hora"] + (p["duracion"] // 100) * 60 + (p["duracion"] % 100)
            if (nueva_hora < hora_fin and nueva_hora_fin > p["hora"]):
                return False

    if control_horario:
        if "Documental" in peli["genero"] and nueva_hora >= 2200:
            return False
        if "Drama" in peli["genero"] and nuevo_dia == "Viernes":
            return False
        if nuevo_dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"] and (nueva_hora >= 2300 or nueva_hora < 600):
            return False

    return True

def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:

    if edad_invitado >= 18:
        return True
    if edad_invitado < 15 and 'Terror' in peli['genero']:
        return False
    if edad_invitado <= 10 and 'Familiar' not in peli['genero']:
        return False
    clasificacion = peli['clasificacion']

    if clasificacion.isdigit():
        clasificacion_num = int(clasificacion)
    elif '+' in clasificacion:
        clasificacion_num = int(clasificacion[:-1])
    else:
        clasificacion_num = 18
    if edad_invitado < clasificacion_num and peli['genero'] != 'Documental':
        return autorizacion_padres
    return True

