def main():
    my_graph = Graph(8)
    
    # Deffine the graph
    # --------------------
    my_graph.add_edge(0, 1)
    my_graph.add_edge(1, 2)
    my_graph.add_edge(2, 3)
    my_graph.add_edge(3, 0)

    my_graph.add_edge(2, 4)
    
    my_graph.add_edge(4, 5)
    my_graph.add_edge(5, 6)
    my_graph.add_edge(6, 4)
    
    my_graph.add_edge(6, 7)
    # --------------------

    my_graph.print_graph()
    
    a, b = 0, 8
    path_a_b = dfs(my_graph, a, b)
    print(f"Path form a to b: {path_a_b}")

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

def dfs(graph, starting_node, target_node, explored_nodes = [], ab_path = []):
    print()
    print(f"{starting_node}")
    print(f"{explored_nodes}")
    explored_nodes.append(starting_node)  

    if starting_node == target_node:
        print("Returning explored nodes")
        return explored_nodes  
    
    for adjacent_node in graph.adjacency_list[starting_node]:
        
        if not adjacent_node in explored_nodes:
            if dfs(graph, adjacent_node, target_node, explored_nodes):
                return explored_nodes

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                     