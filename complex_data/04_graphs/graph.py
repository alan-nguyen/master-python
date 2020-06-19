# Bring in the Vertex class from vertex.py
from vertex import Vertex

class Graph:
  def __init__(self, directed=False):
    self.directed = directed
    self.graph_dict = {}
  
  def add_vertex(self, vertex):
    print(f"Adding {vertex.value}")
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight=0):
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex):
    print(f"You are searching from {start_vertex} to {end_vertex}")
    start = [start_vertex]
    while len(start) > 0:
      current_vertex = start.pop()
      print(current_vertex)

# # --------- Test add_vertex -------------------
# grand_central = Vertex("Grand Central Station")

# railway = Graph()

# print(railway.graph_dict)
# railway.add_vertex(grand_central)
# print(railway.graph_dict)
