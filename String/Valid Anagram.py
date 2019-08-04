import unittest
class Solution:
    '''
    Given two strings s and t , write a function to determine if t is an anagram of s.
    '''
    def isAnagram(self, s, t) :
        return True if ''.join(sorted(s)) == ''.join(sorted(t)) else False

class Test(unittest.TestCase):
    def test_isAnagram(self):
        input1 = "anagram"
        input2 = "nagaram"
        expected = True
        sol = Solution()
        self.assertEqual(sol.isAnagram(input1, input2),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()
            