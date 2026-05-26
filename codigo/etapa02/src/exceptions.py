# Exceção para vértice duplicado
class VertexAlreadyExistsException(Exception):
    pass


# Exceção para vértice inexistente
class VertexNotFoundException(Exception):
    pass


# Exceção para aresta duplicada
class EdgeAlreadyExistsException(Exception):
    pass


# Exceção para loops em grafos simples
class LoopNotAllowedException(Exception):
    pass