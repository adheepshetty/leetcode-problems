import unittest
class Solution:
    '''
    Given a 2d grid map of '1's (land) and '0's (water), 
    count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.
    '''
    def numIslands(self, grid):
        num_of_islands = 0
        # Traverse though the grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if "1" is found that means we have found a root node
                if grid[row][col] == "1":
                    # increment count of number of islands as we have found an island
                    num_of_islands +=1
                    # check for its surrounding using dfs approach
                    self.island_dfs(grid, row, col)
        
        return num_of_islands
    
    def island_dfs(self, grid, row, column):
        # if the row is less than 0 or greater than the last value or column is less than 0 or greater than the last value of column stop recursion and return nothing
        if (not 0 <= row <= len(grid)-1) or (not 0 <= column <= len(grid[0])-1): return
    
        # if the grid[row][column] is not equal to 1 that mean it is water so return nothing
        elif grid[row][column] != '1': return 
        
        else:
            # once land found and visited mark it's value as 0 and check it neighbouring values using dfs approach
            grid[row][column] = "0"
            self.island_dfs(grid, row-1, column)
            self.island_dfs(grid, row+1, column)
            self.island_dfs(grid, row, column-1)
            self.island_dfs(grid, row, column+1)
        

class Test(unittest.TestCase):
    def test_numIslands(self):
        data = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
        expected = 3
        sol = Solution()
        self.assertEqual(sol.numIslands(data),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()