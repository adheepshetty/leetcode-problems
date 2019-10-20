import unittest
class Solution:
    '''
    Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

    Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

    If S[i] == "I", then A[i] < A[i+1]
    If S[i] == "D", then A[i] > A[i+1]
    

    Example 1:

    Input: "IDID"
    Output: [0,4,1,3,2]
    Example 2:

    Input: "III"
    Output: [0,1,2,3]
    Example 3:

    Input: "DDI"
    Output: [3,2,0,1]
    '''
    def diStringMatch(self, S):
        s = list(range(len(S)+1))
        res = []
        for c in S:
            if c == 'I':
                res.append(s.pop(0))
            else:
                res.append(s.pop())
        res.append(s.pop())
        return res
    
class Test(unittest.TestCase):
    def test_diStringMatch(self):
        S = "IDID"
        res = [0,4,1,3,2]
        sol = Solution()
        self.assertEqual(sol.diStringMatch(S),res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()