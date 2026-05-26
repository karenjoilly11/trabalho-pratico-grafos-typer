# Implementação de grafo utilizando matriz de adjacência.
# A matriz indica se existe aresta entre dois vértices.

from codigo.etapa02.src.AbstractGraph import AbstractGraph
from codigo.etapa02.src.exceptions import LoopNotAllowedException

class AdjacencyMatrixGraph(AbstractGraph):

    def __init__(self, num_vertices):

        # Inicializa atributos da classe pai
        super().__init__(num_vertices)

        # Cria matriz preenchida com False
        self.matrix = [
            [False for _ in range(num_vertices)]
            for _ in range(num_vertices)
        ]


    def add_edge(self, u, v):

        # Valida índices dos vértices
        self._validate_vertex(u)
        self._validate_vertex(v)

        # Não permite loops
        if u == v:
            raise LoopNotAllowedException(
                "Grafos simples não permitem loops"
            )

        # Adiciona aresta
        self.matrix[u][v] = True


    def remove_edge(self, u, v):

        # Remove aresta
        self.matrix[u][v] = False


    def has_edge(self, u, v):

        # Verifica existência da aresta
        return self.matrix[u][v]


    def get_edge_count(self):

        total = 0

        # Conta arestas da matriz
        for i in range(self.num_vertices):

            for j in range(self.num_vertices):

                if self.matrix[i][j]:
                    total += 1

        return total


    def get_vertex_degree(self, v):

        degree = 0

        # Conta vizinhos do vértice
        for i in range(self.num_vertices):

            if self.matrix[v][i]:
                degree += 1

        return degree


    def is_connected(self):

        visited = set()

        # Executa DFS a partir do vértice 0
        self._dfs(0, visited)

        # Verifica se todos foram visitados
        return len(visited) == self.num_vertices


    def _dfs(self, vertex, visited):

        visited.add(vertex)

        # Percorre vizinhos
        for i in range(self.num_vertices):

            if self.matrix[vertex][i]:

                if i not in visited:
                    self._dfs(i, visited)


    def export_to_gephi(self, path):

        with open(path, "w") as file:

            file.write("Source,Target\n")

            # Exporta arestas
            for u in range(self.num_vertices):

                for v in range(self.num_vertices):

                    if self.matrix[u][v]:

                        file.write(f"{u},{v}\n")


    def _validate_vertex(self, vertex):

        # Verifica se vértice é válido
        if vertex < 0 or vertex >= self.num_vertices:

            raise IndexError(
                "Vértice inválido"
            )