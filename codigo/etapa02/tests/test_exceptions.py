# Importa implementação do grafo
from codigo.etapa02.src.AdjacencyListGraph import AdjacencyListGraph

# Importa exceção personalizada
from codigo.etapa02.src.exceptions import LoopNotAllowedException


# Cria grafo com 3 vértices
graph = AdjacencyListGraph(3)


try:

    # Tenta criar loop
    graph.add_edge(0, 0)

except LoopNotAllowedException as error:

    # Exibe mensagem da exceção
    print(error)