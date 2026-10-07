# Atividade 02 - Teoria de Grafos
# Problema: a partir do Centro de Distribuição, encontrar a rota de menor
# custo até cada posto da rede logística.
# Isso é um problema de Caminho Mínimo, resolvido aqui com o
# Algoritmo de Dijkstra.

import heapq

# Arestas do mapa: (origem, destino, custo)
# O grafo é não direcionado: a estrada vale nos dois sentidos.
arestas = [
    ("Posto 1", "Posto 2", 8),
    ("Posto 1", "Posto 3", 10),
    ("Posto 2", "Distribuidora", 6),
    ("Posto 3", "Posto 4", 6),
    ("Posto 3", "Distribuidora", 8),
    ("Posto 3", "Posto 6", 12),
    ("Posto 4", "Posto 5", 7),
    ("Posto 4", "Posto 6", 9),
    ("Posto 5", "Posto 6", 10),
    ("Posto 5", "Posto 7", 8),
    ("Distribuidora", "Posto 6", 14),
    ("Distribuidora", "Posto 8", 4),
    ("Distribuidora", "Posto 9", 5),
    ("Posto 6", "Posto 7", 6),
    ("Posto 6", "Posto 10", 5),
    ("Posto 6", "Posto 11", 9),
    ("Posto 7", "Posto 12", 7),
    ("Posto 8", "Posto 9", 10),
    ("Posto 8", "Posto 13", 12),
    ("Posto 9", "Posto 10", 7),
    ("Posto 9", "Posto 13", 4),
    ("Posto 10", "Posto 11", 10),
    ("Posto 10", "Posto 13", 8),
    ("Posto 11", "Posto 12", 8),
    ("Posto 12", "Posto 14", 6),
    ("Posto 13", "Posto 14", 12),
]

# Monta a lista de adjacência: para cada vértice, seus vizinhos e custos
grafo = {}
for origem, destino, custo in arestas:
    grafo.setdefault(origem, []).append((destino, custo))
    grafo.setdefault(destino, []).append((origem, custo))


def dijkstra(grafo, inicio):
    # Distância mínima conhecida até cada vértice (começa "infinita")
    distancia = {v: float("inf") for v in grafo}
    distancia[inicio] = 0

    # Guarda de onde viemos, para reconstruir o caminho depois
    anterior = {v: None for v in grafo}

    # Fila de prioridade: sempre pega o vértice mais próximo ainda não visitado
    fila = [(0, inicio)]
    visitados = set()

    while fila:
        dist_atual, atual = heapq.heappop(fila)

        if atual in visitados:
            continue
        visitados.add(atual)

        # Relaxamento: tenta melhorar a distância dos vizinhos passando por "atual"
        for vizinho, custo in grafo[atual]:
            nova_dist = dist_atual + custo
            if nova_dist < distancia[vizinho]:
                distancia[vizinho] = nova_dist
                anterior[vizinho] = atual
                heapq.heappush(fila, (nova_dist, vizinho))

    return distancia, anterior


def montar_caminho(anterior, destino):
    """Volta do destino até a origem seguindo o dicionário 'anterior'."""
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = anterior[atual]
    return list(reversed(caminho))


inicio = "Distribuidora"
distancia, anterior = dijkstra(grafo, inicio)

# Ordena os postos pelo número para exibir bonitinho
postos = sorted(
    (v for v in grafo if v != inicio),
    key=lambda nome: int(nome.split()[1]),
)

print(f"Rotas de menor custo a partir da {inicio}:\n")
for posto in postos:
    caminho = " -> ".join(montar_caminho(anterior, posto))
    print(f"{posto:>8}: custo {distancia[posto]:>2} | {caminho}")