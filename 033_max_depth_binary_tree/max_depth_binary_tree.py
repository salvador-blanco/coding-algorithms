from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], max_depth_count = None) -> int:
        if max_depth_count == None:
            max_depth_count = 0
            if not root:
                return 0
        
        max_depth_count += 1
        
        if root.left == None and root.right == None:
            return max_depth_count

        left_depth = self.maxDepth(root.left, max_depth_count) if root.left else max_depth_count
        right_depth = self.maxDepth(root.right, max_depth_count) if root.right else max_depth_count
        
        return max(left_depth, right_depth)
        
def main():
    balanced_tree = balanced_tree_lvl_3()
    unbalanced_tree = unbalanced_tree_lvl_3()
    tester = Solution()
    print(tester.maxDepth(balanced_tree))
    print(tester.maxDepth(unbalanced_tree))

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