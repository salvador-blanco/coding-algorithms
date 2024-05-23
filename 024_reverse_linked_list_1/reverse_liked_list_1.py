from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return head

    
def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next

def main():
    # Test case 1: [1,2,3,4,5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    tester = Solution()
    print("---")
    print_linked_list(head)
    print("---")
    reversed_head = tester.reverseList(head)
    print_linked_list(reversed_head)

if __name__ == "__main__":
    main()
