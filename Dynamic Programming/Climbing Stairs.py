import unittest
class Solution(object):
    '''
    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    '''
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib = nxt = 1
        for _ in range(n):
            fib, nxt = nxt, fib + nxt
        
        return fib

class Test(unittest.TestCase):
    def test_isAnagram(self):
        input = 5
        expected = 8
        sol = Solution()
        self.assertEqual(sol.climbStairs(input),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()
            