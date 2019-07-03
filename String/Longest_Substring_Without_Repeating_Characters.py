import unittest
class Solution(object):
    '''
    Given a string, find the length of the longest substring without repeating characters.
    '''
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        list = ""
        for i in range(len(s)):
            if s[i] in list:
                list = list[list.index(s[i])+1:]
            list +=s[i]
            length = max(length, len(list))
        return length

class Test(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        s = "abcabcbb"
        expected = 3
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring(s),expected)

        

if __name__ == "__main__":
    unittest.main()