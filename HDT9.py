#Universidad del Valle de Guatemala
#Algoritmos y Estrucuras de Datos
#Felipe Aguilar - 23195
#Fernando Rueda - 23748



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