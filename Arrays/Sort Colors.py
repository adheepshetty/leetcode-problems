import unittest
# author: Adheep
class Solution:
    '''
    Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

    Note: You are not suppose to use the library's sort function for this problem.

    Example:

    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    Follow up:

    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
    Could you come up with a one-pass algorithm using only constant space?
    '''
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # low handles "0"
        # mid moves and handles "1"
        # high handles "2"
        low = mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low] , nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1: 
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

   
class Test(unittest.TestCase):
    def test_sortColors(self):
        data = [2,0,2,1,1,0]
        expected = [0,0,1,1,2,2]
        sol = Solution()
        self.assertEqual(sol.sortColors(data),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()