from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        tortoise_node, hare_node = head, head

        while True:
            
            if not hare_node.next:
                return None
            elif not hare_node.next.next:
                return None
            
            tortoise_node = tortoise_node.next
            hare_node = hare_node.next.next
            
            if tortoise_node == hare_node:
                hare_node = head
                while hare_node != tortoise_node:
                    hare_node = hare_node.next
                    tortoise_node = tortoise_node.next
                return hare_node
    
def main():
    tester = Solution()
    test_case_one = create_linked_list_with_cycle([2,13,-24,21,23,-21,5], -1)
    print_linked_list(test_case_one)
    cycle_node_one = tester.detectCycle(test_case_one)
    if cycle_node_one:
        print(cycle_node_one.val)
    else:
        print("No cycle")

def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current_node = head
    nodes = [head]
    for value in values[1:]:
        new_node = ListNode(value)
        current_node.next = new_node
        current_node = new_node
        nodes.append(new_node)
    
    if pos != -1:
        current_node.next = nodes[pos]
    
    return head

def print_linked_list(head: ListNode, max_iterations=60):
    current = head
    count = 0
    while current and count < max_iterations:
        print(f"{current.val} -> ", end="")
        current = current.next
        count += 1    

        
if __name__ == "__main__":
    main()