import unittest
class Solution:
    '''
    Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

    Example:

    Input: 3
    Output:
    [
        [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]
    ]
    '''
    def generateMatrix(self, n):
        grid = [[-1]*n for a in range(n)]
        val = 1
        i , j = 0, 0
        while val<= n*n:
            while j<= n-1 and grid[i][j] == -1:
                grid[i][j] = val
                j +=1
                val += 1
            j -=1
            i +=1
            while i<=n-1 and grid[i][j] == -1:
                grid[i][j] = val
                i += 1
                val += 1
            i -=1
            j -=1
            while j <= n-1 and grid[i][j] == -1:
                grid[i][j] = val
                j -=1
                val += 1
            i -=1
            j +=1
            while i<=n-1 and grid[i][j] == -1:
                grid[i][j] = val
                i -= 1
                val += 1
            i +=1
            j +=1
        return grid


class Test(unittest.TestCase):
    def test_generateMatrix(self):
        n = 3       
        expected = [[1,2,3],[8,9,4],[7,6,5]]
        sol = Solution()
        self.assertEqual(sol.generateMatrix(n), expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main() 