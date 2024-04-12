import pdb
import random
import math

def main():
    a_graph = Graph(5, False)
    a_graph.add_edge(0,1)
    a_graph.add_edge(1,2)
    a_graph.add_edge(2,3)
    a_graph.add_edge(3,4)


    print()
    print("Original graph:")
    a_graph.print_graph()
    remaining_nodes = kargers_run(a_graph)
    print("Remaining nodes:")
    print(remaining_nodes)

# iterations = graph.num_nodes**2*math.ln(graph.num_nodes)
# for _ in range(iterations):
def kargers_run(graph):
    while graph.num_nodes > 2:
        n1, n2 = graph.select_random_edge()
        graph.fuse_nodes(n1, n2)
    return graph.adjacency_list



class Graph():
    def __init__(self, num_nodes, directed = True):
        self.num_nodes = num_nodes
        self.nodes = range(num_nodes)
        #dictionary
        self.adjacency_list = {node: set() for node in self.nodes}
        self.directed = directed

    def add_edge(self, node1, node2):
        self.adjacency_list[node1].add((node2))
        if not self.directed:
            self.adjacency_list[node2].add((node1))

    def select_random_edge(self):
        node1 = random.choice(list(self.adjacency_list.keys()))
        node2 = random.choice(list(self.adjacency_list[node1]))
        return node1, node2

    def fuse_nodes(self, node1_key, node2_key):
        self.adjacency_list[node1_key].update(self.adjacency_list[node2_key])
        supernode = self.adjacency_list[node1_key]
        supernode.remove(node1_key)
        supernode.remove(node2_key)
        self.adjacency_list.pop(node1_key)
        self.adjacency_list.pop(node2_key)
        
        supernode_key = str(node1_key) + "," + str(node2_key)
        self.adjacency_list[supernode_key] = supernode
        for node_key in self.adjacency_list.keys():
            if node2_key in self.adjacency_list[node_key]:
                self.adjacency_list[node_key].remove(node2_key)
                self.adjacency_list[node_key].add(supernode_key)
            if node1_key in self.adjacency_list[node_key]:
                self.adjacency_list[node_key].remove(node1_key)
                self.adjacency_list[node_key].add(supernode_key)
        self.num_nodes -= 1

    def print_graph(self):
        for node_key in self.adjacency_list.keys():
            print(f"node {node_key}: {self.adjacency_list[node_key]}")


if __name__ == "__main__":
    main()