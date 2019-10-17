import unittest
class Solution:
    '''

    For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

    Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

    

    Example 1:

    Input: A = [1,2,0,0], K = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234
    Example 2:

    Input: A = [2,7,4], K = 181
    Output: [4,5,5]
    Explanation: 274 + 181 = 455
    Example 3:

    Input: A = [2,1,5], K = 806
    Output: [1,0,2,1]
    Explanation: 215 + 806 = 1021
    Example 4:

    Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
    Output: [1,0,0,0,0,0,0,0,0,0,0]
    Explanation: 9999999999 + 1 = 10000000000

    '''

    def addToArrayForm(self, A, K):
        a=int(''.join(str(i) for i in A))
        res, ans=a+K, []
        for i in str(res):
            ans.append(int(i))
        return ans

class Test(unittest.TestCase):
    def test_addToArrayForm(self):
        A = [2,7,4]
        K = 181
        expected = [4,5,5]
        sol = Solution()
        self.assertEqual(sol.addToArrayForm(A, K),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()