import unittest
import re
class Solution:
    '''
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
    '''
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        return re.match('^'+p+'$', s) != None

class Test(unittest.TestCase):
    def test_isMatch(self):
        data = "aa"
        p = "a*"
        expected = True
        sol = Solution()
        self.assertEqual(sol.isMatch(data, p),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()