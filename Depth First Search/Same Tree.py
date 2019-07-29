import unittest
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
        Given two binary trees, write a function to check if they are the same or not.

        Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
    '''
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==q==None:
            return True
        if None in [p,q]:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

class Test(unittest.TestCase):
    def test_deleteDuplicates(self):
        tree1 = TreeNode(1)
        tree1.left = TreeNode(2)
        tree1.right = TreeNode(3)

        tree2 = TreeNode(1)
        tree2.left = TreeNode(2)
        tree2.right = TreeNode(3)

        res = True
        sol = Solution()
        self.assertEqual(sol.isSameTree(tree1, tree2), res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()