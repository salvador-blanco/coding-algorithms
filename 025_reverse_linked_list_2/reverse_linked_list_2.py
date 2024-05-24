from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        phantom_node = ListNode(None, head) 
        left_pointer = phantom_node
        
        for _ in range(left-1):
            left_pointer = left_pointer.next    

        previous_node = left_pointer.next
        current_node = previous_node.next
     
        for _ in range(right-left):
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        left_pointer.next.next = current_node
        left_pointer.next = previous_node

        return phantom_node.next
        
def print_linked_list(head :ListNode):
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next
    print("Null")

def main():
    head = ListNode(1, ListNode(2, ListNode(3,ListNode(4,ListNode(5)))))
    tester = Solution()
    print("original list: ", end = "")
    print_linked_list(head)
    reversed_head = tester.reverseBetween(head, 1,5)
    print_linked_list(reversed_head)

if __name__ == "__main__":
    main()

