from typing import Optional

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':        
        if not head:
            return head

        insertion_pointers = []
        current_node = head
        while True:
            if current_node.child:
                insertion_pointers.append(current_node)
                current_node = current_node.child
            elif current_node.next:
               current_node = current_node.next
            elif not current_node.next and insertion_pointers:
                insertion_node = insertion_pointers.pop()
                if insertion_node.next:
                    current_node.next = insertion_node.next
                    current_node.next.prev = current_node
                else:
                   current_node.next = None                 

                insertion_node.child.prev = insertion_node 
                insertion_node.next = insertion_node.child
                insertion_node.child = None
            else:
               return head

def main():
    tester = Solution()
    test_case_head = linked_list_test_case_one()
    print("Test case one")
    print("Original graph")
    print_lists(test_case_head)
    result_head = tester.flatten(test_case_head)
    print("Flattened Graph:")
    print_lists(result_head)
    print()
    print("Test case two")
    print("Original graph")
    test_case_head = linked_list_test_case_two()
    print_lists(test_case_head)
    result_head = tester.flatten(test_case_head)
    print("Flattened Graph:")
    print_lists(result_head)

class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def linked_list_test_case_one():
    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)

    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node3.child = node7
    node4.prev = node3
    node4.next = node5
    node5.prev = node4
    node5.next = node6
    node6.prev = node5

    node7.next = node8
    node8.prev = node7
    node8.next = node9
    node8.child = node11
    node9.prev = node8
    node9.next = node10
    node10.prev = node9

    node11.next = node12
    node12.prev = node11
    return node1

def linked_list_test_case_two():
    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.prev = node1
    node2.child = node3
    node3.child = node4   

    return node1



def str_lists(head, lists):
  '''
  from https://replit.com/@karencfisher/doublelist#main.py
  Helper function to recursively serialize the graph prior to visualization. It's an interim step and
  only meant to be called by the printLists function.

  Parameters:
    head - head of the present list 
    lists - the serialization being built recursively (passed by reference)

  Returns:
    None (lists is updated in place). 
  '''
  if head is None:
    return
  nodes = []
  while head:
    nodes.append(str(head.val))
    if head.child is not None:
      nodes.append('|')
      str_lists(head.child, lists)
    head = head.next
  lists.append(nodes)

def print_lists(head):
  '''
  from https://replit.com/@karencfisher/doublelist#main.py
  Visualizes the entire graph
  Parameter:
    head - the top most Node
  '''
  lists = []
  str_lists(head, lists)
  if lists == []:
    print(None)
    return
  previndent = 0
  for j, l in enumerate(lists[::-1]):
    count = -1
    indent = 0
    s = []
    for i in range(len(l)):
      if l[i] != '|':
        s.append(l[i])
        count += 1
      else:
        indent = count * 4
        child = count
    print('---'.join(s)) 
    if  len(lists) > 1 and j < len(lists) - 1:
      previndent += indent
      indentation = ''.join([' '] * previndent)
      if len(l[0]) > 1:
        indentation += ''.join([' '] * child)
      print(indentation + '|')
      print(indentation, end='')

if __name__ == "__main__":
    main()
        