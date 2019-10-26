# author: Adheep
import unittest
import math
class Solution(object):
    '''
    In an infinite binary tree where every node has two children, the nodes are labelled in row order.

    In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

    Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.
    
    Example 1:

    Input: label = 14
    Output: [1,3,4,14]
    Example 2:

    Input: label = 26
    Output: [1,2,6,10,26]
    '''
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        
        level = int(math.ceil(math.log(label+1,2)))
        res = []
        
        while label != 0:
            MAX_label = int(2**(level)-1)
            # print(MAX_label)
            MIN_label = int(2**(level-1))
            # print(MIN_label)
            prev_label = ((MAX_label + MIN_label) - label) // 2
            # print(label)
            res.append(label)
            level -=1
            label = prev_label
    
        return res[::-1]

class Test(unittest.TestCase):
    def test_pathInZigZagTree(self):
        n = 14   
        expected = [1,3,4,14]
        sol = Solution()
        self.assertEqual(sol.pathInZigZagTree(n), expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()