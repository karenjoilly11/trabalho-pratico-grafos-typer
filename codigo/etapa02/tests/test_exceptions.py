# Importa implementação do grafo
from src.AdjacencyListGraph import AdjacencyListGraph

# Importa exceção personalizada
from src.exceptions import LoopNotAllowedException


# Cria grafo com 3 vértices
graph = AdjacencyListGraph(3)


try:

    # Tenta criar loop
    graph.add_edge(0, 0)

except LoopNotAllowedException as error:

    # Exibe mensagem da exceção
    print(error)