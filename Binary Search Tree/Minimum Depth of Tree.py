# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import unittest

class Solution(object):
    '''
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

    Note: A leaf is a node with no children.

    Example:

    Given binary tree [3,9,20,null,null,15,7],

         3
        / \
       9  20
         /  \
       15    7
    return its minimum depth = 2.

    '''
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        if not ((root.left) or (root.right)): return 1
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if not ((node.left) or (node.right)): 
                print(node.val)
                return level
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
                
        return level
    
class Test(unittest.TestCase):
    def test_minDepth(self):
        expected = 2
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        sol = Solution()
        self.assertEqual(sol.minDepth(root),expected)

   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()