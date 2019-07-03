import unittest
class Solution(object):
    '''Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.'''
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target:
                    if i!=j:
                        return [i,j]

class Test(unittest.TestCase):
    def test_twosum(self):
        data = [2, 7, 11, 15]
        target = 9
        expected = [0,1]
        sol = Solution()
        self.assertEqual(sol.twoSum(data, target),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()