# Definition for a binary tree node.
import unittest
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
    A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
    '''
    def isSubtree(self, s, t):
        if not s: return False
        if self.isSameTree(s, t):return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSameTree(self, p , q):
        if p and q: return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

    def test_(self):
        root1 = TreeNode(3)
        root1.left = TreeNode(4)
        root1.right = TreeNode(5)
        root2 = TreeNode(3)
        root2.left = TreeNode(4)
        root2.right = TreeNode(5)
        sol = Solution()
        self.assertEqual(sol.isSubtree(root1, root2),True)
        # queue, res = [t1], []
        # while queue:
        #     node = queue.pop(0)
        #     res.append(node.val)
        #     if node.left: queue.append(node.left)
        #     if node.right: queue.append(node.right)
        # print(res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()