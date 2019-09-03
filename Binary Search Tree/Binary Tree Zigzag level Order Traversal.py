import unittest
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
    '''
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level+1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(curr.val)
                else:
                    res[level].insert(0, curr.val)
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return res 

class Test(unittest.TestCase):
    def test_zigzagLevelOrder(self):
        expected = [[3], [20,9], [15,7]]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        sol = Solution()
        self.assertEqual(sol.zigzagLevelOrder(root),expected)

   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()