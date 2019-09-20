import unittest
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# author: Adheep
class Solution:
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        if not t1:
            return t2
        return t1


class Test(unittest.TestCase):
    def test_mergeTrees(self):
        root1 = TreeNode(3)
        root1.left = TreeNode(4)
        root1.right = TreeNode(5)
        root2 = TreeNode(3)
        root2.left = TreeNode(4)
        root2.right = TreeNode(4)
        root2.left.left = TreeNode(5)
        sol = Solution()
        t1 = sol.mergeTrees(root1, root2)
        queue, res = [t1], []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        print(res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()