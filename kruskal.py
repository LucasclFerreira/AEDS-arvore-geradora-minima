class Grafo:
    def __init__(self):
        self.numero_vertices = 0
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
            self.numero_vertices += 1

    def adicionar_aresta(self, origem, destino):
        if origem in self.grafo and destino in self.grafo:
            self.grafo[origem].append(destino)
            self.grafo[destino].append(origem)

    def obter_adjacentes(self, vertice):
        if vertice in self.grafo:
            return self.grafo[vertice]
        else:
            return []

    def exibir_grafo(self):
        for vertice in self.grafo:
            adjacentes = self.grafo[vertice]
            print(f"Vertice {vertice}: {adjacentes}")


# Exemplo de uso
grafo = Grafo()

# Adicionando vértices
grafo.adicionar_vertice(0)
grafo.adicionar_vertice(1)
grafo.adicionar_vertice(2)
grafo.adicionar_vertice(3)

# Adicionando arestas
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 2)
grafo.adicionar_aresta(0, 3)
grafo.adicionar_aresta(3, 2)
grafo.adicionar_aresta(2, 1)

# Exibindo o grafo
grafo.exibir_grafo()
