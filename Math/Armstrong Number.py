import unittest

class Solution:
    '''
    The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

    Given a positive integer N, return true if and only if it is an Armstrong number.

    

    Example 1:

    Input: 153
    Output: true
    Explanation: 
    153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
    Example 2:

    Input: 123
    Output: false
    Explanation: 
    123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
    '''
    def isArmstrong(self, N):
        return N == sum([int(x)**len(str(N)) for x in list(str(N))])

class Test(unittest.TestCase):
    def test_isArmstrong(self):
        num = 153
        res = True
        sol = Solution()
        self.assertEqual(sol.isArmstrong(num),res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()