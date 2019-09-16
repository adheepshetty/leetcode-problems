# author: Adheep
# Definition for a binary tree node.
import unittest
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

        Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.
    '''
    def findMode(self, root):
        if not root: return []
        stack = [root]
        nodeval_count = {}
        while stack:
            node = stack.pop()
            if node.val in nodeval_count: nodeval_count[node.val] +=1
            else: nodeval_count[node.val] = 1
            if not node.left and not node.right: continue
            if node.left:
                stack.append(node.left)
                # print(node.left)
            if node.right:
                stack.append(node.right)
        max_val = max([val for val in nodeval_count.values()])
        res = []
        for key,val in nodeval_count.items():
            if val == max_val:
                res.append(key)
        return res

class Test(unittest.TestCase):
    def test_findMode(self):
        expected = [2]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(2)
        sol = Solution()
        self.assertEqual(sol.findMode(root),expected)

   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()