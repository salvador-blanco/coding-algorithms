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

def generate_graph_2():
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

def generate_graph_1():
    graph = Graph(5)
    
    # Deffine the graph
    # --------------------
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)

    graph.add_edge(1, 3)
    graph.add_edge(1, 4)

    graph.add_edge(2, 3)
    graph.add_edge(4, 3)


    # --------------------
    return graph

if __name__ == "__main__":
    main()