import unittest
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

    Note: A leaf is a node with no children.

    Example:

    Given binary tree [3,9,20,null,null,15,7],
    '''
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue, res, temp, level_prev = [(root, 0)], [], [], 0
        if not root: return 0
        while queue:
            node, level = queue.pop(0)
            if level_prev != level:
                res.append(temp)
                temp = []
            temp.append(node.val)
            level_prev = level
            if node.left: queue.append((node.left, level+1))
            if node.right:queue.append((node.right, level+1))
        res.append(temp)
        return level+1

class Test(unittest.TestCase):
    def test_maxDepth(self):
        expected = 3
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        sol = Solution()
        self.assertEqual(sol.maxDepth(root),expected)

   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()