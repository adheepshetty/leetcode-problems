import unittest
class Solution:
    '''
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
    '''

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        ind = 0
        try:
            while True:
                letter = strs[0][ind]
                for word in strs:
                    if letter != word[ind]:
                        return prefix
                prefix += letter
                ind += 1
        except IndexError:
            return prefix

class Test(unittest.TestCase):
    def test_longestCommonPrefix(self):
        data = ["flower","flow","flight"]
        expected = "fl"
        sol = Solution()
        self.assertEqual(sol.longestCommonPrefix(data),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()