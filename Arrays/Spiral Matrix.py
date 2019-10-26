import unittest
class Solution(object):
    '''
    Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

    Example 1:

    Input:
    [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]
    Example 2:

    Input:
    [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    '''
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        m = len(matrix)
        n = len(matrix[0])
        if m == 1: return [i for i in matrix[0]]
        if n == 1: return [j for i in range(len(matrix)) for j in matrix[i]]
        flatten_matrix = []
        i , j = 0, 0
        while matrix[i][j] not in flatten_matrix:
            while j <= n-1  and matrix[i][j] not in flatten_matrix:
                flatten_matrix.append(matrix[i][j])
                j +=1
            j -=1
            i +=1
            while i <= m-1  and matrix[i][j] not in flatten_matrix:
                flatten_matrix.append(matrix[i][j])
                i += 1
            i -=1
            j -=1
            while j >= 0  and matrix[i][j] not in flatten_matrix:
                flatten_matrix.append(matrix[i][j])
                j -=1
            i -=1
            j +=1
            while i >= 0 and matrix[i][j] not in flatten_matrix:
                flatten_matrix.append(matrix[i][j])
                i -= 1
            i +=1
            j +=1
        return flatten_matrix
        

class Test(unittest.TestCase):
    def test_spiralOrder(self):    
        n = [[1,2,3],[8,9,4],[7,6,5]]
        expected = [1,2,3,6,9,8,7,4,5]
        sol = Solution()
        self.assertEqual(sol.spiralOrder(n), expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()
