from heapq import heappop, heappush
from math import inf

def dijkstras(graph, start):
  distances = {}
  # Set all vertices' distaces to inf
  for vertex in graph:
    distances[vertex] = inf
  distances[start] = 0
  # List contains tuple of distance and vertex
  vertices_to_explore = [(0, start)]

