from collections import defaultdict, deque

class CityGraph:
  def __init__(self):
    self.connections = defaultdict(list)

  def add_route(self, city1, city2):
    self.connections[city1].append(city2)
    self.connections[city2].append(city1) # Undirected route

  def breadth_first_search(self, start_city, end_city):
    """Finds a path between two cities using Breadth-First Search."""
    visited = {start_city}
    queue = deque([(start_city, [start_city])]) # Store path along with city

    while queue:
      current_city, path = queue.popleft()
      if current_city == end_city:
        return path # Path found

      for neighbor in self.connections[current_city]:
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append((neighbor, path + [neighbor]))

    return None # No path found

  def depth_first_search(self, start_city, end_city, visited=None):
    """Finds a path between two cities using Depth-First Search (Recursive)."""
    if visited is None:
      visited = set()

    visited.add(start_city)
    if start_city == end_city:
      return [start_city] # Path found

    for neighbor in self.connections[start_city]:
      if neighbor not in visited:
        path = self.depth_first_search(neighbor, end_city, visited)
        if path:
          return [start_city] + path # Prepend start city to path

    return None # No path found

def read_city_connections(file_path):
  """Reads city connections from a file and builds a CityGraph."""
  city_map = CityGraph()
  with open(file_path, "r") as file:
    next(file) # Skip the header
    for line in file:
      city1, city2 = line.strip().split(",")
      city_map.add_route(city1, city2)
  return city_map

if __name__ == "__main__":
  city_graph = read_city_connections("cities.txt")

  start_city = "New York"
  end_city = "San Francisco" # Choose a destination city

  print("\nBreadth-First Search (BFS):")
  bfs_path = city_graph.breadth_first_search(start_city, end_city)
  if bfs_path:
    print(f"Path found: {' -> '.join(bfs_path)}")
  else:
    print("No path found.")

  print("\nDepth-First Search (DFS):")
  dfs_path = city_graph.depth_first_search(start_city, end_city)
  if dfs_path:
    print(f"Path found: {' -> '.join(dfs_path)}")
  else:
    print("No path found.")
