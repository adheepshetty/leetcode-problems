import unittest
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.
    '''
    prev, branch = float("inf"), float("-inf")
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return root
        self.minDiffInBST(root.left)
        self.prev, self.branch = min(self.prev, root.val - self.branch), root.val
        self.minDiffInBST(root.right)
        
        return self.prev

class Test(unittest.TestCase):
    def test_minDiffInBST(self):
        expected = 1
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        sol = Solution()
        self.assertEqual(sol.minDiffInBST(root),expected)

   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()