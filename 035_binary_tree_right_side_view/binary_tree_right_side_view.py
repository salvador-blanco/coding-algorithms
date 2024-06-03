from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode], depth_count = None, traversal = None) -> int:
        if depth_count == None:
            depth_count, traversal = 0, []
            
            if not root:
                return []

        if len(traversal) == depth_count:
            traversal.append(root.val)

        if root.right and root != None:
            self.rightSideView(root.right, depth_count + 1, traversal)
        if root.left and root != None:
            self.rightSideView(root.left, depth_count + 1, traversal)  
        
        return traversal
        
        
def main():
    balanced_tree = balanced_tree_lvl_3()
    unbalanced_tree = unbalanced_tree_lvl_3()
    tester = Solution()
    print(tester.rightSideView(balanced_tree))
    print(tester.rightSideView(unbalanced_tree))
    print(tester.rightSideView([]))

def balanced_tree_lvl_3():
    leaf07 = TreeNode(7)
    leaf08 = TreeNode(8)
    
    leaf09 = TreeNode(9)
    leaf10 = TreeNode(10)

    leaf11 = TreeNode(11)
    leaf12 = TreeNode(12)

    leaf13 = TreeNode(13)
    leaf14 = TreeNode(14)

    node3 = TreeNode(3, leaf07, leaf08)
    node4 = TreeNode(4, leaf09, leaf10)
    node5 = TreeNode(5, leaf11, leaf12)
    node6 = TreeNode(6, leaf13, leaf14)

    node1 = TreeNode(1, node3, node4)
    node2 = TreeNode(2, node5, node6)

    return TreeNode(0, node1, node2)

def unbalanced_tree_lvl_3():
    leaf3 = TreeNode(3)
    
    node2 = TreeNode(2, leaf3, None)
    
    node1 = TreeNode(1, node2, None)

    return TreeNode(0, node1, None)



if __name__ == "__main__":
    main()