import unittest
class Solution(object):
    '''
    Given a column title as appear in an Excel sheet, return its corresponding column number.

    For example:

        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28 
        ...
    Example 1:

    Input: "A"
    Output: 1
    Example 2:

    Input: "AB"
    Output: 28
    Example 3:

    Input: "ZY"
    Output: 701
    '''
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res += ((ord(s[len(s) - i - 1]) - ord('A') + 1)*(26**i))
        
        return res
    

class Test(unittest.TestCase):
    def test_titleToNumber(self):
        data = "AB"
        expected = 28
        sol = Solution()
        self.assertEqual(sol.titleToNumber(data),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()