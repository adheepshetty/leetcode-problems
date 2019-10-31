import unittest
# author: Adheep
class Solution(object):
    '''
    Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

    Example:

    Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
    Output: [3,3,5,5,6,7] 
    Explanation: 

    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
    1 [3  -1  -3] 5  3  6  7       3
    1  3 [-1  -3  5] 3  6  7       5
    1  3  -1 [-3  5  3] 6  7       5
    1  3  -1  -3 [5  3  6] 7       6
    1  3  -1  -3  5 [3  6  7]      7
    '''
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return list()
        queue, res = [], []
        
        for i in range(k):
            while queue and queue[-1][0] <= nums[i]:
                queue.pop()
            queue.append((nums[i], i))
            
        res.append(queue[0][0])
            
        for i in range(k , len(nums)):
            if i - queue[0][1] >= k:
                queue.pop(0)
            
            while queue and queue[-1][0] <= nums[i]:
                queue.pop()
            queue.append((nums[i], i))
            
            res.append(queue[0][0])
            
        return res

class Test(unittest.TestCase):
    def test_maxSlidingWindow(self):
        data = [1,3,-1,-3,5,3,6,7]
        k = 3
        expected = [3,3,5,5,6,7] 
        sol = Solution()
        self.assertEqual(sol.maxSlidingWindow(data, k),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()