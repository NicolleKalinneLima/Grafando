# Atividade 03 - Teoria de Grafos
# Problema: agendar os exames finais de 6 disciplinas sem que duas
# disciplinas com alunos em comum caiam no mesmo período.
# Isso é um problema de Coloração de Grafos: cada cor é um período,
# e vértices vizinhos (disciplinas em conflito) não podem ter a mesma cor.
# O menor número de cores possível é o número cromático do grafo.

# Vértices (disciplinas)
disciplinas = ["Matemática", "Português", "História", "Geografia", "Física", "Química"]

# Arestas: pares de disciplinas que têm alunos em comum (conflito)
conflitos = [
    ("Matemática", "Português"),
    ("Matemática", "História"),
    ("Matemática", "Geografia"),
    ("Português", "História"),
    ("Português", "Física"),
    ("História", "Geografia"),
    ("História", "Física"),
    ("Geografia", "Química"),
    ("Física", "Química"),
]

# Lista de adjacência
grafo = {d: [] for d in disciplinas}
for a, b in conflitos:
    grafo[a].append(b)
    grafo[b].append(a)


def pode_colorir(vertice, cor, cores):
    """Verifica se nenhum vizinho do vértice já usa essa cor."""
    return all(cores.get(vizinho) != cor for vizinho in grafo[vertice])


def colorir(indice, k, cores):
    """Backtracking: tenta colorir os vértices um a um usando no máximo k cores."""
    if indice == len(disciplinas):
        return True  # todas as disciplinas receberam um período

    vertice = disciplinas[indice]
    for cor in range(1, k + 1):
        if pode_colorir(vertice, cor, cores):
            cores[vertice] = cor
            if colorir(indice + 1, k, cores):
                return True
            del cores[vertice]  # desfaz a escolha e tenta a próxima cor

    return False


def numero_cromatico():
    """Testa k = 1, 2, 3... e retorna o primeiro k que funciona.
    Como testamos do menor para o maior, o resultado é garantidamente o mínimo."""
    for k in range(1, len(disciplinas) + 1):
        cores = {}
        if colorir(0, k, cores):
            return k, cores


k, cores = numero_cromatico()

print(f"Número mínimo de períodos: {k}\n")
for periodo in range(1, k + 1):
    materias = [d for d in disciplinas if cores[d] == periodo]
    print(f"Período {periodo}: {', '.join(materias)}")