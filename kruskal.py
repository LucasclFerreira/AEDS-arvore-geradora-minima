class Grafo:
    def __init__(self):
        self.numero_vertices = 0
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = {}
            self.numero_vertices += 1

    def adicionar_aresta(self, origem, destino, peso):
        if origem in self.grafo and destino in self.grafo:
            self.grafo[origem][destino] = peso
            self.grafo[destino][origem] = peso

    def obter_adjacentes(self, vertice):
        if vertice in self.grafo:
            return self.grafo[vertice]
        else:
            return {}

    def exibir_grafo(self):
        for vertice in self.grafo:
            adjacentes = self.grafo[vertice]
            print(f"Vertice {vertice}: {adjacentes}")
    
    def kruskal(self):
        # conjunto vazio para inicializar o kruskal
        conjunto = []

        # preenchendo conjunto com os vertices isolados
        for vertice in range(self.numero_vertices):
            conjunto.append(self.grafo[vertice])
        print(conjunto)

        # iterando por cada aresta no grafo
        for vertice in conjunto:
            for key, value in vertice.items():
                print(key, value)
        


# Exemplo de uso
grafo = Grafo()

# Adicionando vértices
grafo.adicionar_vertice(0)
grafo.adicionar_vertice(1)
grafo.adicionar_vertice(2)
grafo.adicionar_vertice(3)

# Adicionando arestas
grafo.adicionar_aresta(0, 1, 2)
grafo.adicionar_aresta(0, 2, 1)
grafo.adicionar_aresta(0, 3, 3)
grafo.adicionar_aresta(3, 2, 4)
grafo.adicionar_aresta(2, 1, 7)

# Exibindo o grafo
grafo.exibir_grafo()

# kruskal
grafo.kruskal()
