# Definition for a binary tree node.
import unittest
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# author: Adheep
class Solution:
    '''
    Given a binary tree, return all root-to-leaf paths.

    Note: A leaf is a node with no children.

    Example:

    Input:

       1
     /   \
    2     3
     \
      5

    Output: ["1->2->5", "1->3"]

    Explanation: All root-to-leaf paths are: 1->2->5, 1->3
    '''
    def binaryTreePaths(self, root):
        if not root: return []
        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path+'->'+str(node.left.val)))
            if node.right:
                stack.append((node.right, path+'->'+str(node.right.val)))
        
        return paths

class Test(unittest.TestCase):
    def test_binaryTreePaths(self):
        expected = ["1->3", "1->2->5"]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(None)
        root.left.right = TreeNode(5)
        sol = Solution()
        self.assertEqual(sol.binaryTreePaths(root),expected)

   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()