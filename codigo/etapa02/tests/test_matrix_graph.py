# Importa implementação do grafo por matriz de adjacência
from codigo.etapa02.src.AdjacencyMatrixGraph import AdjacencyMatrixGraph


# Cria grafo com 5 vértices
graph = AdjacencyMatrixGraph(5)


# Adiciona arestas ao grafo
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)


# Verifica se existe aresta entre 0 e 1
print(graph.has_edge(0, 1))


# Exibe quantidade total de arestas
print(graph.get_edge_count())


# Exibe grau do vértice 0
print(graph.get_vertex_degree(0))


# Verifica se o grafo é conectado
print(graph.is_connected())


# Exporta grafo para visualização no Gephi
graph.export_to_gephi(
    "grafo_matriz.csv"
)

print("Exportação concluída!")