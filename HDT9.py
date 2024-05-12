#Universidad del Valle de Guatemala
#Algoritmos y Estrucuras de Datos
#Felipe Aguilar - 23195
#Fernando Rueda - 23748

import networkx as nx
import matplotlib.pyplot as plt

def leer_rutas(archivo):
    """ Función para cargar las rutas desde un archivo en un grafo, eliminando espacios extra. """
    grafo = nx.Graph()
    with open(archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip().replace('“', '').replace('”', '')
            partes = linea.split(',')
            origen, destino, costo = partes[0].strip('" ').strip(), partes[1].strip('" ').strip(), int(partes[2])
            grafo.add_edge(origen, destino, weight=costo)
            grafo.add_edge(destino, origen, weight=costo)  # Asegura que el grafo sea no dirigido
    return grafo

def mostrar_rutas(grafo, origen):
    """ Muestra las rutas más cortas desde una estación de origen y las dibuja """
    try:
        caminos, costos = nx.single_source_dijkstra(grafo, origen)
        for destino, ruta in caminos.items():
            costo = costos[destino]
            print(f"Desde {origen} a {destino}: Ruta {ruta}, Costo: {costo}")
    except nx.NetworkXNoPath:
        print("No hay ruta disponible.")
    except KeyError:
        print("Estación no encontrada.")

    def graficar_grafo(grafo, origen, caminos):
    """ Función para graficar el grafo con un camino específico resaltado """
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_size=700, node_color='lightblue')
    # Asegura que caminos contenga listas de nodos
    if all(isinstance(path, list) for path in caminos.values()):
        ruta_especifica = [edge for path in caminos.values() for edge in zip(path[:-1], path[1:])]
        nx.draw_networkx_edges(grafo, pos, edgelist=ruta_especifica, edge_color='red', width=2)
    plt.show()

# Programa principal
def main():
    grafo = leer_rutas("rutas.txt")
    while True:
        print(f"Estaciones disponibles: {list(grafo.nodes())}")
        estacion_origen = input("Ingrese el nombre de su estación de salida: ").strip()
        try:
            caminos, _ = nx.single_source_dijkstra(grafo, estacion_origen)
            mostrar_rutas(grafo, estacion_origen)
            graficar_grafo(grafo, estacion_origen, caminos)
        except nx.NodeNotFound:
            print("Error: La estación ingresada no se encuentra en el grafo. Por favor verifique y pruebe de nuevo.")
        if input("¿Desea seguir consultando rutas? (si/no): ").lower() != 'si':
            break

if _name_ == "_main_":
    main()