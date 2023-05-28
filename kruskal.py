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
    
    def remover_aresta(self, origem, destino):
        if origem in self.grafo and destino in self.grafo:
            del self.grafo[origem][destino]
            del self.grafo[destino][origem]


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
        conjuntos = []
        arestas = []
        agm = self.grafo
        for vertice in self.grafo:
            conjuntos.append(set([vertice]))
        print(conjuntos)
        for origem, adjacentes in self.grafo.items():
            for destinatario in adjacentes.items():
                destinatario = tuple([origem]) + destinatario
                arestas.append(destinatario)
        arestasOrdenadas = sorted(arestas, key=lambda x:x[2])
        for aresta in arestasOrdenadas:
            conjunto1 = self.conjuntoDe(aresta[0], conjuntos)
            conjunto2 = self.conjuntoDe(aresta[1], conjuntos)
            # print("arestas:", aresta[0], aresta[1])
            # print("conjuntos:", conjunto1, conjunto2)
            if conjunto1 != conjunto2:
                conjuntos = self.aplicarUniao(self.conjuntoDe(aresta[0], conjuntos), self.conjuntoDe(aresta[1], conjuntos), conjuntos)
        return conjuntos
    
    def aplicarUniao(self, origem, destino, conjuntos):
        print("conjuntos:", origem, destino)
        if origem in conjuntos:
            conjuntos.remove(origem)
        if destino in conjuntos:
            conjuntos.remove(destino)
        uniao = origem | destino
        print(uniao)
        conjuntos.append(uniao)
        print("conj resultante:", conjuntos)
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
