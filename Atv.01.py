# Atividade 01 - Teoria de Grafos
# Problema: interligar 5 escritórios com o menor custo total de cabeamento.
# Isso é um problema de Árvore Geradora Mínima (AGM / MST),
# resolvido aqui com o Algoritmo de Kruskal.

# Vértices (escritórios)
vertices = ["Campinas", "Leme", "Americana", "Sumaré", "Hortolândia"]

# Arestas: (origem, destino, custo em milhões de R$)
arestas = [
    ("Campinas", "Leme", 4),
    ("Campinas", "Americana", 2),
    ("Leme", "Americana", 1),
    ("Leme", "Sumaré", 5),
    ("Americana", "Sumaré", 8),
    ("Americana", "Hortolândia", 10),
    ("Sumaré", "Hortolândia", 2),
    ("Leme", "Hortolândia", 6),
]

# Estrutura Union-Find: guarda a qual "grupo" cada vértice pertence,
# para saber se adicionar uma aresta formaria um ciclo.
pai = {v: v for v in vertices}


def encontrar(v):
    """Retorna o representante do grupo de v."""
    while pai[v] != v:
        v = pai[v]
    return v


def unir(a, b):
    """Junta os grupos de a e b."""
    pai[encontrar(a)] = encontrar(b)


def kruskal(vertices, arestas):
    # 1. Ordena as arestas pelo custo (da mais barata para a mais cara)
    arestas_ordenadas = sorted(arestas, key=lambda aresta: aresta[2])

    agm = []
    custo_total = 0

    # 2. Percorre as arestas e só aceita as que não formam ciclo
    for origem, destino, custo in arestas_ordenadas:
        if encontrar(origem) != encontrar(destino):
            unir(origem, destino)
            agm.append((origem, destino, custo))
            custo_total += custo

        # 3. Uma árvore com n vértices tem exatamente n - 1 arestas
        if len(agm) == len(vertices) - 1:
            break

    return agm, custo_total


agm, custo_total = kruskal(vertices, arestas)

print("Conexões escolhidas:")
for origem, destino, custo in agm:
    print(f"  {origem} - {destino}: R$ {custo}M")

print(f"\nCusto total mínimo: R$ {custo_total}M")