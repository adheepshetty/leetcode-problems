# author: Adheep
import unittest
class Solution:
    '''
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.

    Your algorithm's runtime complexity must be in the order of O(log n).

    Example 1:

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
    '''
    # author: Adheep
    def search(self, nums, target):
        
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
        
        def binary_search(low, high):
            while low <= high:
                pivot = (low + high) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        high = pivot - 1
                    else:
                        low = pivot + 1
            return -1
        
        n = len(nums)
        
        if n==0: return -1
        if n==1: return 0 if nums[0] == target else -1
        
        
        rotate_index = find_rotate_index(0, n - 1)
        
        if nums[rotate_index] == target:
            return rotate_index
        if rotate_index == 0:
            return binary_search(0, n - 1)
        if target < nums[0]:
            return binary_search(rotate_index, n-1)
        low, high = 0, len(nums)-1
        return binary_search(0, rotate_index)
        
        
    
class Test(unittest.TestCase):
    def test_find_rotate_index(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        expected = 4
        sol = Solution()
        self.assertEqual(sol.search(nums, target),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()
        
        