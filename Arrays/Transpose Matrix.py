import unittest
class Solution(object):
    '''
    Given a matrix A, return the transpose of A.

    The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.


    '''
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(len(A))] for j in range(len(A[0]))]
        for i in range(len(A[0])):
            for j in range(len(A)):
                    res[i][j] = A[j][i]
        return res

class Test(unittest.TestCase):
    def test_transpose(self):    
        actual = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [[1,4,7],[2,5,8],[3,6,9]]
        sol = Solution()
        self.assertEqual(sol.transpose(actual), expected)

if __name__ == '__main__':
    sol = Solution()
    print(sol.__doc__)
    unittest.main()
    