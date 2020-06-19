class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}
  
  def add_edge(self, vertex):
    print(f"Adding edge to {vertex}")
    self.edges[vertex] = True

  def get_edges(self):
    return list(self.edges.keys())

# # Create an instance
# station = Vertex("Cronk")
  

