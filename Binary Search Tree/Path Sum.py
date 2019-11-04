import unittest
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# author: Adheep
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
#         stack = [(root, sum)]
#         while stack:
#             node, sum = stack.pop()
#             sum -= node.val
#             if sum == 0 and not node.left and not node.right:
#                 return True
#             if node.right:
#                 stack.append((node.right, sum))
#             if node.left:
#                 stack.append((node.left, sum))
                
#         return False
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
                
class Test(unittest.TestCase):
    def test_hasPathSum(self):
        expected = True
        root = TreeNode(2)
        root.left = TreeNode(5)
        root.right = TreeNode(20)
        root.left.left = TreeNode(15)
        root.right.right = TreeNode(7)
        sum = 22
        sol = Solution()
        self.assertEqual(sol.hasPathSum(root, sum),expected)

   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()