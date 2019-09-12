import unittest
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        word_count = {}
        for sp in "!?',;.":
            paragraph = paragraph.replace(sp, ' ')
        for word in paragraph.lower().split():
            if word not in banned:
                if word in word_count:
                    word_count[word] +=1
                else:
                    word_count[word] = 1
        max = 0
        for key, val in word_count.items():
            if val > max:
                max = val
                maxcount_key = key
        return maxcount_key

class Test(unittest.TestCase):
    def test_mostCommonWord(self):
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        expected = "ball"
        sol = Solution()
        self.assertEqual(sol.mostCommonWord(paragraph, banned),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()