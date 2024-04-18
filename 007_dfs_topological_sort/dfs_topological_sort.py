import copy
import graphs

def main():
    my_graph = graphs.generate_graph_2()

    print("Graph: ")
    my_graph.print_graph()
    
    topological_sequence = dfs_topological_sort(my_graph)
    print("\nResults:")
    print(f"topological_sequence: {topological_sequence}")
    
def dfs_topological_sort(graph):
    unsen_nodes = list(copy.deepcopy(graph.nodes))
    topological_sequence = []

    while unsen_nodes:
        node = unsen_nodes[0]
        if node in unsen_nodes:
            topological_sequence += dfs(graph, node, unsen_nodes, [])   
            topological_sequence.append(node)
            unsen_nodes.remove(node)
    
    return list(reversed(topological_sequence))


def dfs(graph, starting_node, unsen_nodes, current_path):
    
    for adjacent_node in graph.adjacency_list[starting_node]: 
        if adjacent_node in unsen_nodes:
             
            unsen_nodes.remove(adjacent_node)
            dfs(graph, adjacent_node, unsen_nodes, current_path) 
            current_path.append(adjacent_node)  
    
    return current_path



if __name__ == "__main__":
    main()