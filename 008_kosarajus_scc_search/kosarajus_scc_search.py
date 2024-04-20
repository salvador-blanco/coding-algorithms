import copy

def main():
    my_graph = generate_graph_2()

    print("Graph: ")
    my_graph.print_graph()

    first_dfs_traversal = run_dfs(my_graph, 3) #DFS first run
    print(f"\nFirst trasversal: {first_dfs_traversal}")
    
    reversed_graph = my_graph.reverse_graph()
    fcc = run_dfs(reversed_graph, first_dfs_traversal[0], True, first_dfs_traversal, [])
    print(f"\nfcc: {fcc}")
 

def run_dfs(graph , starting_node , second_dfs_run = False, unexplored_nodes = None, visited_sequence = None):
    if unexplored_nodes == None:
        unexplored_nodes = list(copy.deepcopy(graph.nodes))
        visited_sequence =[]
    
    
    unexplored_nodes.remove(starting_node)  

    for adjacent_node in graph.adjacency_list[starting_node]: 
        if adjacent_node in unexplored_nodes:
            if run_dfs(graph, adjacent_node, second_dfs_run, unexplored_nodes, visited_sequence):
                return visited_sequence  
    visited_sequence.append(starting_node)

    if unexplored_nodes:
        starting_node = unexplored_nodes[0]

        if second_dfs_run:
            visited_sequence.append('*')

        run_dfs(graph, starting_node,second_dfs_run, unexplored_nodes, visited_sequence)
        return visited_sequence


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

