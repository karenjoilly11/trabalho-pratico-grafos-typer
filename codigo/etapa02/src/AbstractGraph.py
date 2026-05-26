# Classe abstrata base para implementações de grafos.
# Define os métodos obrigatórios da API.
from abc import ABC, abstractmethod


class AbstractGraph(ABC):

    def __init__(self, num_vertices):

        # Valida quantidade de vértices
        if num_vertices <= 0:
            raise ValueError(
                "Número de vértices deve ser maior que zero"
            )

        self.num_vertices = num_vertices


    @abstractmethod
    def add_edge(self, u, v):
        pass


    @abstractmethod
    def remove_edge(self, u, v):
        pass


    @abstractmethod
    def has_edge(self, u, v):
        pass


    @abstractmethod
    def get_edge_count(self):
        pass


    @abstractmethod
    def get_vertex_degree(self, v):
        pass


    @abstractmethod
    def is_connected(self):
        pass


    @abstractmethod
    def export_to_gephi(self, path):
        pass