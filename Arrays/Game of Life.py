import unittest
class Solution:
    # author: Adheep
    '''
    According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

    Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

    Example:

    Input: 
    [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
    ]
    Output: 
    [
    [0,0,0],
    [1,0,1],
    [0,1,1],
    [0,1,0]
    ]
    '''
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        alive = [([(i,j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j]==1])]
        dead = [([(i,j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j]==0])]
        changes = []
        for space in alive:
            for r,c in space:
                # print("r","c",r,c)
                adjacent = [(r+1, c), (r-1,c), (r,c+1), (r,c-1), (r+1,c+1), (r-1,c-1), (r-1, c+1), (r+1,c-1)]
                sum = 0
                for i, j in adjacent:
                    if 0 <= i < len(board) and 0 <= j < len(board[0]):
                        sum += board[i][j]
                if sum < 2 or sum > 3:
                    # Under and Over Population
                    changes.append([r,c,0])
        for space in dead:
            for r,c in space:
                adjacent = [(r+1, c), (r-1,c), (r,c+1), (r,c-1), (r+1,c+1), (r-1,c-1),(r-1, c+1), (r+1,c-1)]
                sum = 0
                for i, j in adjacent:
                    if 0 <= i < len(board) and 0 <= j < len(board[0]):
                        sum += board[i][j]
                if sum == 3:
                    # Reproduction
                    changes.append([r,c,1])
        while changes:
            (i,j,chg) = changes.pop(0)
            board[i][j] = chg
        return board

class Test(unittest.TestCase):
    def test_gameOfLife(self):
        data = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        expected = [[0,0,0], [1,0,1], [0,1,1], [0,1,0]]
        sol = Solution()
        self.assertEqual(sol.gameOfLife(data),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()        
            