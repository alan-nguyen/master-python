class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}
  
  def add_edge(self, vertex, weight=0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

# # Create an instance
# station = Vertex("Cronk")
  
grand_central = Vertex('Grand Central Station')
forty_second_street = Vertex('42nd Street Station')

print(grand_central.get_edges())

# call .add_edge()
grand_central.add_edge(forty_second_street.value)
print(grand_central.get_edges())
