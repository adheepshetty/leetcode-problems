import unittest
class Solution:
    '''
    Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

'''
    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n:
            m >>=1
            n >>=1
            i += 1
        return n << i

class Test(unittest.TestCase):
    def test_rangeBitwiseAnd(self):
        m = 5
        n = 7
        expected = 4
        sol = Solution()
        self.assertEqual(sol.rangeBitwiseAnd(m,n),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()