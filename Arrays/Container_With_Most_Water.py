import unittest
class Solution(object):
    '''
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
    '''
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L,R, width, res = 0, len(height) -1, len(height)-1 , 0
        for i in range(width, 0 , -1):
            if height[L] < height[R]:
                res, L= max(res , height[L]*i),L+1
            else:
                res, R = max(res, height[R]*i), R-1
                
        return res

class Test(unittest.TestCase):
    def test_maxArea(self):
        data = [1,8,6,2,5,4,8,3,7]
        expected = 49
        sol = Solution()
        self.assertEqual(sol.maxArea(data),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()