# Implementação de grafo utilizando lista de adjacência.
# Cada vértice armazena seus vértices vizinhos.

from codigo.etapa02.src.AbstractGraph import AbstractGraph

from codigo.etapa02.src.exceptions import LoopNotAllowedException

class AdjacencyListGraph(AbstractGraph):

    def __init__(self, num_vertices):

        super().__init__(num_vertices)

        # Lista de adjacência
        # Cada vértice possui um conjunto de vizinhos
        self.graph = {
            i: set()
            for i in range(num_vertices)
        }


    def add_edge(self, u, v):

        # Valida índices
        self._validate_vertex(u)
        self._validate_vertex(v)

        # Não permite loops
        if u == v:
            raise LoopNotAllowedException(
                "Grafos simples não permitem loops"
        )

        # Set evita arestas paralelas automaticamente
        self.graph[u].add(v)


    def remove_edge(self, u, v):

        self.graph[u].discard(v)


    def has_edge(self, u, v):

        return v in self.graph[u]


    def get_edge_count(self):

        total = 0

        for vertex in self.graph:
            total += len(self.graph[vertex])

        return total


    def get_vertex_degree(self, v):

        return len(self.graph[v])


    def is_connected(self):

        visited = set()

        self._dfs(0, visited)

        return len(visited) == self.num_vertices


    def _dfs(self, vertex, visited):

        visited.add(vertex)

        for neighbor in self.graph[vertex]:

            if neighbor not in visited:
                self._dfs(neighbor, visited)


    def export_to_gephi(self, path):

        with open(path, "w") as file:

            file.write("Source,Target\n")

            for u in self.graph:

                for v in self.graph[u]:

                    file.write(f"{u},{v}\n")


    def _validate_vertex(self, vertex):

        if vertex < 0 or vertex >= self.num_vertices:

            raise IndexError(
                "Vértice inválido"
            )