import unittest
class Solution:
    """
        Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
        """
    def isPalindrome(self, x):
        
        return str(x)[:] == str(x)[::-1]


class Test(unittest.TestCase):
    def test_isPalindrome(self):
        data = 121
        expected = True
        sol = Solution()
        self.assertEqual(sol.isPalindrome(data),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()