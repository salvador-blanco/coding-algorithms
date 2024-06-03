from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        depth_right = self.get_left_depth(root.right)
        depth_left  = self.get_left_depth(root.left)

        if depth_right == depth_left:
            return pow(2,depth_left) + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + pow(2,depth_right) 
        
    def get_left_depth(self, node, depth = 0):
        while node:
            depth += 1
            node = node.left
        return depth

def main():
    t1 = tree_1()
    t2 = tree_2()
    tester = Solution()

    t1_r = tester.countNodes(t1)
    t2_r = tester.countNodes(t2)

    print()
    print(t1_r)
    print(t2_r)

def tree_1():
    #[1,2,3,4]
    leaf04 = TreeNode(4)
    node2 = TreeNode(2, leaf04, None)
    node3 = TreeNode(3, None, None)
    return TreeNode(1, node2, node3)

#       1
#      / \
#     2   3
#    /
#   4

def tree_2():
    #[1,2,3,4,5,6]
    leaf04 = TreeNode(4)
    leaf05 = TreeNode(5)
    leaf06 = TreeNode(6)

    node2 = TreeNode(2, leaf04, leaf05)
    node3 = TreeNode(3, leaf06, None)
    return TreeNode(1, node2, node3)

#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

if __name__ == "__main__":
    main()