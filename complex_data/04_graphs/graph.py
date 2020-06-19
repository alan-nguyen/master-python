# Bring in the Vertex class from vertex.py
from vertex import Vertex

class Graph:
  def __init__(self, directed=False):
    self.directed = directed
    self.graph_dict = {}
  
