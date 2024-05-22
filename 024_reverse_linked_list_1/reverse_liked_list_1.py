from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            head.next.next
        except AttributeError:
            return head
        
        current_node = head
        next_node = head.next
        current_node.next = None
        while next_node.next:
            temp_node = next_node
            next_node = temp_node.next
            temp_node.next = current_node
            current_node = temp_node
        next_node.next = current_node

        return next_node
    
def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next

def main():
    # Test case 1: [1,2,3,4,5]
    head = ListNode(1,ListNode(1))
    tester = Solution()
    print_linked_list(head)
    reversed_head = tester.reverseList(head)
    print_linked_list(reversed_head)

if __name__ == "__main__":
    main()
