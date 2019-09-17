# author: Adheep
import unittest
class Solution:
    '''
    Implement pow(x, n), which calculates x raised to the power n (xn).
    '''
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -n
        result = 1
        while n:
            if n & 1:
                result *= x
            x *= x
            n = n//2
        return result
    
class Test(unittest.TestCase):
    def test_reverse(self):
        data = 2.00000
        power = 10
        expected = 1024.00000
        sol = Solution()
        self.assertEqual(sol.myPow(data, power),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()