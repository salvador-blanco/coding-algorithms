def main():
    my_graph = generate_graph()
    print("--------------------")
    print("Print graph: ")
    my_graph.print_graph()
    
    print()
    print("--------------------")
    a, b = 0, 9
    path_a_b = dfs_find_path(my_graph, a, b)
    print(f"Path form {a} to {b}: {path_a_b}")

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

def generate_graph():
    graph = Graph(10)
    
    # Deffine the graph
    # --------------------
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)

    graph.add_edge(2, 4)
    
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 4)
    
    graph.add_edge(6, 7)
    graph.add_edge(6, 8)
    graph.add_edge(6, 9)
    # --------------------
    return graph


def dfs_find_path(graph, starting_node, target_node, explored_nodes = [], ab_path = []):
    explored_nodes.append(starting_node)  

    if not ab_path:
        ab_path.append(starting_node)

    if starting_node == target_node:
        return ab_path  
    
    for adjacent_node in graph.adjacency_list[starting_node]: 
        if not adjacent_node in explored_nodes:
            ab_path.append(adjacent_node)
            if dfs_find_path(graph, adjacent_node, target_node, explored_nodes, ab_path):
                return ab_path
            else:
                ab_path.pop()

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                     