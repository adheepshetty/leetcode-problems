import unittest
from itertools import combinations
class Solution:

    '''Given a set of distinct integers, nums, return all possible subsets (the power set).

    Note: The solution set must not contain duplicate subsets.
    '''
    def subsets(self, nums):
        result = []
        for i in range(len(nums)+1):
            combs = list(combinations(nums,i))
            result += combs
            
        return ([list(i) for i in result])

class Test(unittest.TestCase):
    def test_subsets(self):
        data = [1,2,3]
        expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        sol = Solution()
        self.assertEqual(sol.subsets(data),expected)
        
    def test_subsets2(self):
        data =[1,2]
        expected = [[1], [2], [1, 2]]
        sol = Solution()
        self.assertEqual(sol.subsets(data),expected)
        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()