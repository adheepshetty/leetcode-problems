# author: Adheep
import unittest
# Boyer-Moore Voting Algorithm
class Solution:
    '''
    Given an array of size n, find the majority element that is whose count is more than half of number of elements
    You may assume that the array is non-empty and the majority element always exist in the array.
    '''
    def majorityElement(self, nums):
        count , candidate = 0 , None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
                

class Test(unittest.TestCase):
    def test_majorityElement(self):
        nums = [1, 3, 3]
        sol = Solution()
        self.assertEqual(sol.majorityElement(nums),3)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()