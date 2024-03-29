import unittest
class Solution:
    '''
    Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.

    Example 1:

    Input: a = "11", b = "1"
    Output: "100"
    Example 2:  

    Input: a = "1010", b = "1011"
    Output: "10101"
    '''
    def addBinary(self, a, b):
        return bin((int(a, 2) + int(b, 2)))[2::]

class Test(unittest.TestCase):
    def test_addBinary(self):
        a = "11"
        b = "1"
        expected = "100"
        sol = Solution()
        self.assertEqual(sol.addBinary(a,b),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()