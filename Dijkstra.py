import heapq

def dijkstra(grafo, inicio, fim):
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[inicio] = 0
    fila_prioridade = [(0, inicio)]

    predecessores = {vertice: None for vertice in grafo}

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))
                predecessores[vizinho] = vertice_atual

    caminho = []
    vertice = fim
    while vertice is not None:
        caminho.append(vertice)
        vertice = predecessores.get(vertice, None)
    
    caminho.reverse()

    if distancias[fim] == float('infinity'):
        caminho = ["Não há caminho"]

    return distancias, caminho

grafo = {
    'Frankfurt': {'Mannheim': 85, 'Wurzburg': 217, 'Kassel': 173},
    'Mannheim': {'Frankfurt': 85, 'Karlsruhe': 80},
    'Karlsruhe': {'Mannheim': 80, 'Augsburg': 250},
    'Augsburg': {'Karlsruhe': 250, 'Munchen': 84},
    'Wurzburg': {'Frankfurt': 217, 'Erfurt': 186, 'Numberg': 103},
    'Erfurt': {'Wurzburg': 186},
    'Numberg': {'Wurzburg': 103, 'Stuttgart': 183, 'Munchen': 167},
    'Stuttgart': {'Numberg': 183}, 
    'Kassel': {'Frankfurt': 173, 'Munchen': 502},
    'Munchen': {'Augsburg': 84, 'Numberg': 167, 'Kassel': 502}
}

inicio = 'Frankfurt'
fim = 'Munchen'

distancias, caminho = dijkstra(grafo, inicio, fim)
print("Menor Distância:", distancias[fim])
print("Caminho:", caminho)
