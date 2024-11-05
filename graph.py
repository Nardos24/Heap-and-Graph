class Graph:
     """
    Represents a graph using an adjacency list.

    This class implements a graph data structure using an adjacency list,
    allowing for representation and manipulation of edges and nodes.
    """
     def __init__(self):
        self.adjacency_list = {}

     def add_edge(self, source, destination):
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []
        self.adjacency_list[source].append(destination)

        if destination not in self.adjacency_list:
            self.adjacency_list[destination] = []
        self.adjacency_list[destination].append(source)

def build_graph(file_path):
     """
    Builds a graph from a file containing edge data.

    The file is assumed to have a header row that is skipped, and each
    subsequent line represents an edge with source and destination nodes
    separated by a comma.

    Args:
        file_path (str): The path to the file containing edge data.

    Returns:
        Graph: The constructed graph object.
    """
     graph = Graph()

     with open(file_path, "r") as file:
        next(file)  # Skip header row
        for line in file:
            source, destination = line.strip().split(",")
            graph.add_edge(source, destination)

     return graph

if __name__ == "__main__":
    graph = build_graph("cities.txt")
    print(graph.adjacency_list)