import unittest
from itertools import product
class Solution:
    '''
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    
    '''

    def letterCombinations(self, digits: str) -> [str]:
        phone_dict = {  "2":"abc",
                        "3":"def",
                        "4":"ghi",
                        "5":"jkl",
                        "6":"mno",
                        "7":"pqrs",
                        "8":"tuv",
                        "9":"wxyz"}
        
        if not digits:return []
        if len(digits) == 1:return list((phone_dict[digits[0]]))
        seen = set()
        combs = list()
        for ch in digits:
            if ch in seen:
                continue 
            combs.append(phone_dict[ch])
        return ["".join(x) for x in product(*combs)]

class Test(unittest.TestCase):
    def test_letterCombinations(self):
        data = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        sol = Solution()
        self.assertEqual(sol.letterCombinations(data),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()