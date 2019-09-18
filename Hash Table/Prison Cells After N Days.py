# author: Adheep
import unittest
class Solution:
    '''
    There are 8 prison cells in a row, and each cell is either occupied or vacant.

    Each day, whether the cell is occupied or vacant changes according to the following rules:

    If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.

    Otherwise, it becomes vacant.
    
    (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

    We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

    Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

    '''
    def prisonAfterNDays(self, cells, N):
        def next_day_cells(cells):
            nextdaycells = [0] *len(cells)
            for i in range(1, len(cells)-1):
                if cells[i-1] and cells[i+1]: nextdaycells[i] = 1
                elif not (cells[i-1] or cells[i+1]): nextdaycells[i] = 1
                else: nextdaycells[i] = 0
            return nextdaycells
        
        if N == 0: return cells
        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N
            if N >= 1:
                N -= 1
                cells = next_day_cells(cells)
        return cells


class Test(unittest.TestCase):
    def test_prisonAfterNDays(self):
        cells = [0,1,0,1,1,0,0,1]
        days = 7
        res =  [0,0,1,1,0,0,0,0]
        sol = Solution()
        self.assertEqual(sol.prisonAfterNDays(cells, days),res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()