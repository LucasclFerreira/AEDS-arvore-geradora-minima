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
        conjuntos = []

        # preenchendo conjunto com os vertices isolados
        for vertice in self.grafo:
            conjuntos.append(set([vertice]))
        print(conjuntos)

        arestas = []
        for origem, adjacentes in self.grafo.items():
            for destinatario in adjacentes.items():
                destinatario = tuple([origem]) + destinatario
                arestas.append(destinatario)

        arestasOrdenadas = sorted(arestas, key=lambda x:x[2])
        print("Arestas ordenadas:", arestasOrdenadas)

        cont = 0
        for aresta in arestasOrdenadas:
            print("CONJUNTO DE V1:", self.conjuntoDe(aresta[0], conjuntos))
            print("CONJUNTO DE V2:", self.conjuntoDe(aresta[1], conjuntos))
            if self.conjuntoDe(aresta[0], conjuntos) != self.conjuntoDe(aresta[1], conjuntos):
                print("os conjuntos são DIFERENTES")
                cont += 1
                conjuntos = self.aplicarUniao(aresta[0], aresta[1], conjuntos)
            print("")
        print(cont)
        return conjuntos
    
    def aplicarUniao(self, origem, destino, conjuntos):
        for conjunto in conjuntos:
            if destino in conjunto:
                conjuntoDestino = conjunto
                conjuntos.remove(conjunto)

        for conjunto in conjuntos:
            if origem in conjunto:
                conjunto.add(conjuntoDestino)
        return conjuntos

    def conjuntoDe(self, vertice, conjuntos):
        for conjunto in conjuntos:
            if vertice in conjunto:
                return conjunto

        
        


# Exemplo de uso
grafo = Grafo()

# Adicionando vértices
grafo.adicionar_vertice(0)
grafo.adicionar_vertice(1)
grafo.adicionar_vertice(2)
grafo.adicionar_vertice(3)
grafo.adicionar_vertice(4)
grafo.adicionar_vertice(5)
grafo.adicionar_vertice(6)
grafo.adicionar_vertice(7)
grafo.adicionar_vertice(8)

# Adicionando arestas
grafo.adicionar_aresta(0, 1, 4)
grafo.adicionar_aresta(0, 7, 8)
grafo.adicionar_aresta(1, 2, 8)
grafo.adicionar_aresta(1, 7, 11)
grafo.adicionar_aresta(2, 3, 7)
grafo.adicionar_aresta(2, 8, 2)
grafo.adicionar_aresta(2, 5, 4)
grafo.adicionar_aresta(3, 5, 14)
grafo.adicionar_aresta(3, 4, 9)
grafo.adicionar_aresta(4, 5, 10)
grafo.adicionar_aresta(5, 6, 2)
grafo.adicionar_aresta(6, 7, 1)
grafo.adicionar_aresta(6, 8, 6)
grafo.adicionar_aresta(7, 8, 7)

# Exibindo o grafo
grafo.exibir_grafo()

# kruskal
agm = grafo.kruskal()
print(agm)
