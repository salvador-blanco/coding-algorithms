import copy

def main():
    my_graph = generate_graph()
    print("--------------------")
    print("Print graph: ")
    my_graph.print_graph()
    
    print()
    print("--------------------")
    topological_sequence = dfs_topological_sort(my_graph)
    print(f"topological_sequence: {topological_sequence}")

def dfs_topological_sort(graph):
    unsen_nodes = list(copy.deepcopy(graph.nodes))
    topological_sequence = []

    for node in graph.nodes:
        if node in unsen_nodes:
            dfs_path = dfs(graph, node, unsen_nodes)
            print(f"Node {node}: {dfs_path}")
            unsen_nodes.remove(node)
    return topological_sequence


def dfs(graph, starting_node, unsen_nodes = [], ab_path = []):

    if not unsen_nodes:
        return ab_path
    
    for adjacent_node in graph.adjacency_list[starting_node]: 
        if adjacent_node in unsen_nodes:
            ab_path.append(adjacent_node)
            unsen_nodes.remove(adjacent_node)
            dfs(graph, adjacent_node, unsen_nodes, ab_path)
            
    
    return ab_path

def generate_graph():
    graph = Graph(6)
    
    # Deffine the graph
    # --------------------
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(4, 1)
    graph.add_edge(4, 0)

    graph.add_edge(5, 0)
    graph.add_edge(5, 2)
    # --------------------
    return graph

class Graph():
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.nodes = range(n_nodes)
        self.adjacency_list = {node:[] for node in self.nodes}
    
    def add_edge(self, node_a, node_b):
        self.adjacency_list[node_a].append(node_b)

    def print_graph(self,):
        for node_key in self.adjacency_list:
            print(f"node: {node_key} adjacent nodes: {self.adjacency_list[node_key]}")

if __name__ == "__main__":
    main()        