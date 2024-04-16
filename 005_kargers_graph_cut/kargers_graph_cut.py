import pdb
import random
import math
import time
import copy
from collections import Counter

def main():
    a_graph = Graph(8, False)

    a_graph.add_edge(0,1)
    a_graph.add_edge(0,2)
    a_graph.add_edge(0,3)
    a_graph.add_edge(1,3)
    a_graph.add_edge(1,2)
    a_graph.add_edge(2,3)

    a_graph.add_edge(3,4)

    a_graph.add_edge(4,5)
    a_graph.add_edge(4,6)
    a_graph.add_edge(4,7)
    a_graph.add_edge(5,6)
    a_graph.add_edge(5,7)
    a_graph.add_edge(6,7)



    print()
    print("Original graph:")
    a_graph.print_graph()
    remaining_nodes = kargers_algorithm(a_graph)
    print(remaining_nodes)

def kargers_run(graph):
    while graph.num_nodes > 2:
        n1, n2 = graph.select_random_edge()
        graph.fuse_nodes(n1, n2)
    return graph.adjacency_list

def kargers_algorithm(graph):
    n_trails = int( (graph.num_nodes**2)*math.log(graph.num_nodes))
    results = []
    for _ in range(n_trails):
         graph_copy = copy.deepcopy(graph)
         result = kargers_run(graph_copy).keys()
         # For each trail sort the neighbors and the remaining nodes
         result = tuple(sorted([tuple(sorted(str(key).split())) for key in result])) 
         results.append(result)
    
    result_frequency = Counter(results)
    most_common = result_frequency.most_common(1)
    return most_common


class Graph():
    def __init__(self, num_nodes, directed = True):
        self.num_nodes = num_nodes
        self.nodes = range(num_nodes)
        #dictionary
        self.adjacency_list = {node: set() for node in self.nodes}
        self.directed = directed
        random.seed(time.time())

    def add_edge(self, node1, node2):
        self.adjacency_list[node1].add((node2))
        if not self.directed:
            self.adjacency_list[node2].add((node1))

    def select_random_edge(self):
        
        node1 = random.choice(list(self.adjacency_list.keys()))
        node2 = random.choice(list(self.adjacency_list[node1]))
        return node1, node2

    def fuse_nodes(self, node1_key, node2_key):
        self.adjacency_list[node1_key].update(self.adjacency_list[node2_key]) # fuse nodes 1 & 2 in node 1
        supernode_neighbors = self.adjacency_list[node1_key] #create a separated variable for the fused nodes
        supernode_neighbors.remove(node1_key) 
        supernode_neighbors.remove(node2_key)

        del self.adjacency_list[node1_key]
        del self.adjacency_list[node2_key]
        
        supernode_key = str(node1_key) + " " + str(node2_key)
        self.adjacency_list[supernode_key] = supernode_neighbors

        for node_key, node_neighbors in self.adjacency_list.items():
            if node1_key in node_neighbors or node2_key in node_neighbors:
                node_neighbors.discard(node1_key)
                node_neighbors.discard(node2_key)
                node_neighbors.add(supernode_key)
        
        # Reduce the number of nodes count        
        self.num_nodes -= 1

    def print_graph(self):
        for node_key in self.adjacency_list.keys():
            print(f"node {node_key}: {self.adjacency_list[node_key]}")


if __name__ == "__main__":
    main()