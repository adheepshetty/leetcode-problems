import unittest
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
    '''
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        temp, res, level_prev = [], [], 0
        if not root:
            return res
        queue = [(root,0)]
        visited = []
        while queue:
            (node, level) = queue.pop(0)
            if level != level_prev:
                res.append(temp)
                temp = []
            temp.append(node.val)   
            level_prev = level
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        
        res.append(temp)
        return res

class Test(unittest.TestCase):
    def test_levelOrder(self):
        expected = [[3], [9,20], [15,7]]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        sol = Solution()
        self.assertEqual(sol.levelOrder(root),expected)

   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()