import unittest
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low , high = 0, x
        
        while low<=high:
            mid = (low+high)//2
            
            if mid*mid >x:
                high = mid-1
            elif mid*mid<x:
                low = mid+1
            else:
                return mid
        
        return high

class Test(unittest.TestCase):
    def test_Sqrt(self):
        data = 8
        expected = 2
        sol = Solution()
        self.assertEqual(sol.mySqrt(data),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()