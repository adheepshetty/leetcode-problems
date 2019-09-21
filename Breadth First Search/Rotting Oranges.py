import unittest
class Solution(object):
    '''
    In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.
    Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
    '''
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        rows , columns = len(grid), len(grid[0])
        
        queue = [([(i,j) for i in range(rows) for j in range(columns) if grid[i][j] == 2], 0)]
        
        
        for rotten, minute in queue:
            res = minute
            temp = []
            for r,c in rotten:
                adjacent = [(r+1, c), (r-1,c),(r,c+1),(r,c-1)]
                for i,j in adjacent:
                    if 0<=i<rows and 0<=j<columns and grid[i][j] == 1:
                        grid[i][j] = 2
                        temp.append((i,j))
            if temp:
                queue.append((temp,minute+1))
                
        if any(1 in i for i in grid):
                return -1
            
        return res

        
class Test(unittest.TestCase):
    def test_orangesRotting(self):
        data = [[2,1,1],[1,1,0],[0,1,1]]
        expected = 4
        sol = Solution()
        self.assertEqual(sol.orangesRotting(data),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()     