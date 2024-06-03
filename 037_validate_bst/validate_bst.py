from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], high = float('inf'), low = -float('inf')) -> bool:
        if root == None:
            return True
        
        if root.val >= high or root.val <= low:
            return False
        else:
            return self.isValidBST(root.left, high = root.val, low = low) and self.isValidBST(root.right, low = root.val, high=high) 

    # def check_sub_BST(self, node, high = float('inf'), low = -float('inf')):
        
    #     if node == None:
    #         return True
        
    #     if node.val >= high or node.val <= low:
    #         return False
    #     else:
    #         return self.check_sub_BST(node.left, high = node.val, low = low) and self.check_sub_BST(node.right, low = node.val, high=high) 



def main():
    tester = Solution()
    t1_valid = valid_bst()
    t2_big_valid = big_valid_bst()
    t3_invalid = invalid_bst()

    print(tester.isValidBST(t1_valid))
    print(tester.isValidBST(t2_big_valid))
    print(tester.isValidBST(t3_invalid))

def valid_bst():
    # [2,1,3]
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    root = TreeNode(2, node1, node3)
    return root

#     2
#    / \
#   1   3

def big_valid_bst():
    # [8,3,10,1,6,null,14,null,null,4,7,13]
    node1 = TreeNode(1)
    node4 = TreeNode(4)
    node7 = TreeNode(7)
    node6 = TreeNode(6, node4, node7)
    node3 = TreeNode(3, node1, node6)
    node13 = TreeNode(13)
    node14 = TreeNode(14, node13)
    node10 = TreeNode(10, None, node14)
    root = TreeNode(8, node3, node10)
    return root

#      8
#     / \
#    3  10
#   / \   \
#  1   6   14
#     / \  /
#    4  7 13

def invalid_bst():
    # [5,1,4,None,None,3,6]
    node3 = TreeNode(3)
    node6 = TreeNode(6)
    node4 = TreeNode(4, node3, node6)
    node1 = TreeNode(1)
    root = TreeNode(5, node1, node4)
    return root

#     5
#    / \
#   1   4
#      / \
#     3   6

if __name__ == "__main__":
    main()