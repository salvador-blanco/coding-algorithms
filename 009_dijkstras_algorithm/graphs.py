def main():
    for i, my_graph in enumerate([generate_graph_1(), generate_graph_2()]):
        print(f"\nGraph {i+1}:")
        my_graph.print_graph()

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

    def reverse_graph(self,):
        new_graph = Graph(len(self.nodes))
        for node, adjacent_nodes in self.adjacency_list.items():
            for adjacent_node in adjacent_nodes:
                new_graph.add_edge(adjacent_node, node)
        return new_graph

def generate_graph_2():
    graph = Graph(8)
    
    # Deffine the graph
    # --------------------
    graph.add_edge(0, 1)
    
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 5)
    graph.add_edge(7, 6)

    # --------------------
    return graph

def generate_graph_1():
    graph = Graph(5)
    
    # Deffine the graph
    # --------------------
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)

    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 2)
    # --------------------
    return graph

if __name__ == "__main__":
    main()