# Definition for a binary tree node.
class TreeNode:
    
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self,node): 
        if self is None: 
            self.val = node.val
        else: 
            if node.val is None:
                return node.val
            elif self.val < node.val: 
                if self.right is None: 
                    self.right = node 
                else: 
                    self.right.insert(node) 
            elif self.val > node.val: 
                if self.left is None: 
                    self.left = node 
                else: 
                    self.left.insert(node) 
            

class Solution:
    '''
    Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.
    '''
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack, res, ssf = [], root, 0   # ssf=SumSoFar
        while root or len(stack):
            while root:
                stack.append(root)
                root = root.right
            
            node = stack.pop()
            ssf += node.val
            node.val = ssf
            root = node.left
        return res

class Test:
    def test_bstToGst():
        data = [1,6,0,2,5,7,None,None,None,3,None,None,None,8]
        expected = [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
        root = TreeNode(4)
        expectedroot = TreeNode(30)
        for i in data:
            root.insert(TreeNode(i))

        for i in expected:
            expectedroot.insert(TreeNode(i))

        sol = Solution()
        actualroot = sol.bstToGst(root)

        if actualroot is None: 
            return

        # Create an empty queue for level order traversal 
        queue = [] 
        result = []
    
        # Enqueue Root and initialize height 
        queue.append(actualroot) 
        result.append(actualroot.val)
    
        while len(queue) > 0: 
            # Print front of queue and remove it from queue 
            node = queue.pop(0) 
            #Enqueue left child 
            

            if node.left is not None: 
                queue.append(node.left) 
                result.append(node.left.val)
            elif node.left is None: 
                result.append(node.left)
    
            # Enqueue right child 
            if node.right is not None: 
                queue.append(node.right) 
                result.append(node.right.val)
            elif node.right is None:
                result.append(node.right)

        print(result)
        # self.assertEqual(sol.bstToGst(root),expectedroot)

   

if __name__ == "__main__":
    print(Solution.__doc__)

    print(Test.test_bstToGst())