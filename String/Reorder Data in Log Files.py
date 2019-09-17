# author: Adheep
import unittest
import heapq
class Solution:
    '''
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

    Note:

    The solution set must not contain duplicate triplets.
    '''
    def reorderLogFiles(self, logs):
        let , dig = [], []
        for log in logs:
            if log.split()[1].isdigit(): dig.append(log)
            else: let.append(log)
        heap = []
        heapq.heapify(heap)
        for line in let:
            heapq.heappush(heap,(line.split()[1:], line.split()[0]))
        res = []
        for i in range(len(heap)):
            res.append(heapq.heappop(heap))
        newres = []
        for let in res:
            newres.append(let[1] + " " + " ".join(let[0]))
        
        newres.extend(dig)
        return newres

class Test(unittest.TestCase):
    def test_reorderLogFiles(self):
        data = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        expected = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        sol = Solution()
        self.assertEqual(sol.reorderLogFiles(data),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()