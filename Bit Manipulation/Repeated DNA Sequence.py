import unittest
class Solution:
    '''
        Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
    '''

    def findRepeatedDnaSequences(self, s):
        res, dic = [], {}
        for i in range(len(s)-9):
            substring = s[i:i+10]
            if substring in dic and dic[substring] == False:
                res.append(substring)
                dic[substring] = True
            elif substring not in dic:
                dic[substring] = False
        return res

class Test(unittest.TestCase):
    def test_findRepeatedDnaSequences(self):
        string = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        expected = ["AAAAACCCCC", "CCCCCAAAAA"]
        sol = Solution()
        self.assertEqual(sol.findRepeatedDnaSequences(string),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()