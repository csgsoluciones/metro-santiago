from collections import deque
from heapq import heappush, heappop

LINEAS = {

    "L1": [
        "San Pablo", "Neptuno", "Pajaritos", "Las Rejas", "Ecuador",
        "San Alberto Hurtado", "Universidad de Santiago",
        "Estación Central", "Unión Latinoamericana", "República",
        "Los Héroes", "La Moneda", "Universidad de Chile",
        "Santa Lucía", "Universidad Católica", "Baquedano",
        "Salvador", "Manuel Montt", "Pedro de Valdivia",
        "Los Leones", "Tobalaba", "El Golf", "Alcántara",
        "Escuela Militar", "Manquehue",
        "Hernando de Magallanes", "Los Dominicos"
    ],

    "L2": [
        "Vespucio Norte", "Zapadores", "Dorsal", "Einstein",
        "Cementerios", "Cerro Blanco", "Patronato",
        "Puente Cal y Canto", "Santa Ana", "Los Héroes",
        "Toesca", "Parque O'Higgins", "Rondizzoni",
        "Franklin", "El Llano", "San Miguel",
        "Lo Vial", "Departamental", "Ciudad del Niño",
        "Lo Ovalle", "El Parrón", "La Cisterna"
    ],

    "L3": [
        "Plaza Quilicura", "Lo Cruzat", "Ferrocarril",
        "Los Libertadores", "Cardenal Caro", "Vivaceta",
        "Conchalí", "Plaza Chacabuco", "Hospitales",
        "Puente Cal y Canto", "Plaza de Armas",
        "Universidad de Chile", "Parque Almagro",
        "Matta", "Irarrázaval", "Monseñor Eyzaguirre",
        "Ñuñoa", "Chile España", "Villa Frei",
        "Plaza Egaña", "Fernando Castillo Velasco"
    ],

    "L4": [
        "Tobalaba", "Cristóbal Colón", "Francisco Bilbao",
        "Príncipe de Gales", "Simón Bolívar",
        "Plaza Egaña", "Los Orientales", "Grecia",
        "Los Presidentes", "Quilín", "Las Torres",
        "Macúl", "Vicuña Mackenna", "Vicente Valdés"
    ],

    "L4A": [
        "Vicuña Mackenna", "Santa Julia",
        "La Granja", "Santa Rosa",
        "San Ramón", "La Cisterna"
    ],

    "L5": [
        "Plaza de Maipú", "Santiago Bueras",
        "Del Sol", "Monte Tabor", "Las Parcelas",
        "Laguna Sur", "Barrancas", "Pudahuel",
        "San Pablo", "Lo Prado", "Blanqueado",
        "Gruta de Lourdes", "Quinta Normal",
        "Cumming", "Santa Ana", "Plaza de Armas",
        "Bellas Artes", "Baquedano",
        "Parque Bustamante", "Santa Isabel",
        "Irarrázaval", "Ñuble",
        "Rodrigo de Araya", "Carlos Valdovinos",
        "Camino Agrícola", "San Joaquín",
        "Pedrero", "Mirador",
        "Bellavista de La Florida",
        "Vicente Valdés"
    ],

    "L6": [
        "Cerrillos", "Lo Valledor",
        "Pedro Aguirre Cerda",
        "Franklin", "Bio Bio",
        "Ñuble", "Estadio Nacional",
        "Ñuñoa", "Inés de Suárez",
        "Los Leones"
    ]
}
grafo = {}

for linea, estaciones in LINEAS.items():

    for i in range(len(estaciones)-1):

        a = estaciones[i]
        b = estaciones[i+1]

        if a not in grafo:
            grafo[a] = []

        if b not in grafo:
            grafo[b] = []

        grafo[a].append((b, linea))
        grafo[b].append((a, linea))


def buscar_estacion(nombre):

    nombre = nombre.lower().strip()

    for estacion in grafo:

        if estacion.lower() == nombre:
            return estacion

    return None


def buscar_ruta(origen, destino):

    cola = []

    # (transbordos, estaciones, estacion_actual, ruta, linea_actual)
    heappush(
        cola,
        (0, 0, origen, [origen], None)
    )

    visitados = set()

    while cola:

        transbordos, estaciones, actual, ruta, linea_actual = heappop(cola)

        if actual == destino:
            return ruta

        estado = (actual, linea_actual)

        if estado in visitados:
            continue

        visitados.add(estado)

        for vecino, linea in grafo[actual]:

            nuevo_transbordo = transbordos

            if linea_actual is not None and linea != linea_actual:
                nuevo_transbordo += 1

            heappush(
                cola,
                (
                    nuevo_transbordo,
                    estaciones + 1,
                    vecino,
                    ruta + [vecino],
                    linea
                )
            )

    return None


def obtener_linea(a, b):

    for vecino, linea in grafo[a]:

        if vecino == b:
            return linea

    return None


def mostrar_ruta(ruta):

    linea_actual = None
    transbordos = 0

    print("\nRUTA ENCONTRADA\n")

    for i in range(len(ruta)-1):

        a = ruta[i]
        b = ruta[i+1]

        linea = obtener_linea(a, b)

        if linea != linea_actual:

            if linea_actual is None:
                print(f"\nINICIO EN {linea}\n")
            else:
                transbordos += 1
                print(f"\nTRANSBORDO A {linea}\n")

        print(f"{a} -> {b}")

        linea_actual = linea

    estaciones = len(ruta)-1
    tiempo = estaciones * 2 + transbordos * 4

    print("\n------------------")
    print("Paradas:", estaciones)
    print("Transbordos:", transbordos)
    print("Tiempo estimado:", tiempo, "minutos")


print("\nMETRO DE SANTIAGO\n")

origen_txt = input("Origen: ")
destino_txt = input("Destino: ")

origen = buscar_estacion(origen_txt)
destino = buscar_estacion(destino_txt)

if origen is None:
    print("Estación no encontrada")
    quit()

if destino is None:
    print("Estación no encontrada")
    quit()

ruta = buscar_ruta(origen, destino)

if ruta:
    mostrar_ruta(ruta)
else:
    print("No existe ruta")
