# author: Adheep
import unittest
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

    If two nodes are in the same row and column, the order should be from left to right.
    '''
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        queue , hashtable= [(root , 0)] , {}
        if not root: return []
        while queue:
            (node , order) = queue.pop(0)
            if order in hashtable: hashtable[order].append(node.val)
            else: 
                hashtable[order] = []
                hashtable[order].append(node.val)
            print(node.val, order)
            if node.left: 
                queue.append((node.left, order + 1))
            if node.right:
                queue.append((node.right, order - 1))       
        res = sorted(hashtable.items() , reverse = True, key = lambda x:x[0])
        
        newres = []
        for order, val in res:
            newres.append(val)
        return newres


class Test(unittest.TestCase):
    def test_verticalOrder(self):
        expected = [[3], [20,9], [15,7]]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        sol = Solution()
        self.assertEqual(sol.verticalOrder(root),expected)

   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()
        