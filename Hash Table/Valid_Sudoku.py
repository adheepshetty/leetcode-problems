import unittest
class Solution:
    def isValidSudoku(self, board):
        valid = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    cur = board[i][j]
                    if (i,cur) in valid or (cur,j) in valid or (i//3,j//3,cur) in valid:
                        return False
                    valid.add((i,cur))
                    valid.add((cur,j))
                    valid.add((i//3,j//3,cur))
        return True

class Test(unittest.TestCase):
    def test_isValidSudoku(self):
        data = [
                ["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ]
        expected = True
        sol = Solution()
        self.assertEqual(sol.isValidSudoku(data),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()