import unittest
class Solution:
    '''
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    '''
    def generateParenthesis(self, n: int):
        res = []
        s = [("(", 1, 0)]
        while s:
            x, l, r = s.pop()
            if l < r or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(x)
            s.append((x+"(", l+1, r))
            s.append((x+")", l, r+1))
        return res
       
class Test(unittest.TestCase):
    def test_generateParenthesis(self):
        data = 3
        expected = ["()()()","()(())","(())()","(()())","((()))"]
        sol = Solution()
        self.assertEqual(sol.generateParenthesis(data),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()