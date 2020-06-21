def dfs(graph, current_vertex, target_value, visited=None):
  if visited is None:
    visited = []
	
  visited.append(current_vertex)
  # Base case
  if current_vertex == target_value:
    return visited
	