# author: Adheep
import unittest
class Solution:
    '''
    Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

    Example 1:

    Input: 
    [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
    Output: 
    [
    [1,0,1],
    [0,0,0],
    [1,0,1]
    ]
    '''
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zero_pos = [(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 0]
        for i, j in zero_pos:
            matrix[i][:] =  [0 for k in range(len(matrix[0]))]
            prev_i = i
            for k in range(len(matrix)):
                matrix[k][j] = 0
                
        return matrix

class Test(unittest.TestCase):
    def test_orangesRotting(self):
        data = [[1,1,1], [1,0,1], [1,1,1]]
        expected = [[1,0,1], [0,0,0], [1,0,1]]
        sol = Solution()
        self.assertEqual(sol.setZeroes(data),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()    