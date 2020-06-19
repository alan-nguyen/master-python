from vertex import Vertex
from graph import Graph

# railway = Graph()

# station_one = Vertex("Ballahoo")
# station_two = Vertex("Penn")

# #Call .add_vertex() here
# railway.add_vertex(station_one)
# railway.add_vertex(station_two)

# #Call .add_edge() here
# railway.add_edge(station_one, station_two)
# print("Edges for {0}: {1}".format(station_one.value, station_one.get_edges()))
# print("Edges for {0}: {1}".format(station_two.value, station_two.get_edges()))

# ------------ Test add_edge with weight
railway = Graph()

callan = Vertex('callan')
peel = Vertex('peel')
harwick = Vertex('harwick')

railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)

railway.add_edge(callan, peel, 12)
railway.add_edge(harwick, callan, 7)
railway.add_edge(peel, harwick)

print(callan.edges)
print(harwick.edges)
print(peel.edges)
