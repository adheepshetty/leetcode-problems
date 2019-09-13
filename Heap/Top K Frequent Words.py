# author: Adheep
import unittest
import heapq
class Solution(object):
    '''
    Given a non-empty list of words, return the k most frequent elements.

    Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
    '''
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        heap = []
        heapq.heapify(heap)
        for key in word_count:
            heapq.heappush(heap, (-word_count[key], key))
        res, newres = [], []
        for i in range(k):
            res.append(heapq.heappop(heap))
        for word in res:
            newres.append(word[1])
        return newres

class Test(unittest.TestCase):
    def test_topKFrequent(self):
        expected = ["i", "love"]
        data = ["i", "love", "leetcode", "i", "love", "coding"]
        k = 2
        sol = Solution()
        self.assertEqual(sol.topKFrequent(data, k),expected)

   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()