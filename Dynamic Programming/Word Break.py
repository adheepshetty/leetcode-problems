import unittest
class Solution:
    '''
    Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

    Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.
    Example 1:

    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".
    '''
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i,len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
        
        return dp[-1]


class Test(unittest.TestCase):
    def test_wordBreak(self):
        input = "leetcode"
        wordDict = ["leet", "code"]
        expected = True
        sol = Solution()
        self.assertEqual(sol.wordBreak(input, wordDict),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()