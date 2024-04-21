import copy
import graphs

def main():
    my_graph = graphs.generate_graph_2()

    print("Graph: ")
    my_graph.print_graph()
    

    for i in my_graph.nodes:

        first_dfs_traversal = run_dfs(my_graph,i) #DFS first run
        print(f"\nFirst run stack: {first_dfs_traversal}")
        reversed_graph = my_graph.reverse_graph()
        fcc = run_dfs(reversed_graph, first_dfs_traversal[-1], True, first_dfs_traversal )
        print(f"{fcc.count('*')+1} FCC: {fcc}")


def run_dfs(graph , starting_node , second_dfs_run = False, unexplored_nodes = None, visited_nodes = None, stack = None):
    if unexplored_nodes == None:
        unexplored_nodes = list(graph.nodes)

    if visited_nodes == None:
        visited_nodes = set()
        stack = []
    
    visited_nodes.add(starting_node)

    for adjacent_node in graph.adjacency_list[starting_node]: 
        if not adjacent_node in visited_nodes:
            if run_dfs(graph, adjacent_node, second_dfs_run, unexplored_nodes, visited_nodes, stack):
                return stack
    
    unexplored_nodes.remove(starting_node)
    stack.append(starting_node)  

    if not unexplored_nodes:
        return stack
    
    if all(n in stack for n in visited_nodes): #Manual jump to another node
        starting_node = unexplored_nodes[-1]

        if second_dfs_run: #Separate SCC
            stack.append('*')

        run_dfs(graph, starting_node,second_dfs_run, unexplored_nodes, visited_nodes, stack)
        return stack
    
if __name__ == "__main__":
    main()

