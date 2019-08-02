import unittest
class Solution(object):
    '''
    Given two strings s and t which consist of only lowercase letters.

    String t is generated by random shuffling string s and then add one more letter at a random position.

    Find the letter that was added in t.
    '''

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum1 , sum2 = 0 , 0
        i , j = 0, 0
        for j in range(len(t)):
            sum1 += ord(t[j])
            try:
                sum2 += ord(s[i])
                i = i+1
            except IndexError:
                continue
        return chr(sum1-sum2)

class Test(unittest.TestCase):
    def test_findTheDifference(self):
        s = "abcd"
        t = "abcde"
        expected = "e"
        sol = Solution()
        self.assertEqual(sol.findTheDifference(s,t),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()