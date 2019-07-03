import unittest
class Solution:
    '''
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
        '''
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        pattern = [[] for i in range(numRows)]
        
        level = 0
        direction = 1
        for i in range(len(s)):
            pattern[level].append(s[i])
            level += direction
            if level == len(pattern):
                level = len(pattern)-2
                direction = -1
            elif level == -1:
                level = 1
                direction = 1
        result = ''
        for line in pattern:
            result += ''.join(line)
        return result

class Test(unittest.TestCase):
    def test_convert(self):
        data = "PAYPALISHIRING"
        numRows = 3
        expected = "PAHNAPLSIIGYIR"
        sol = Solution()
        self.assertEqual(sol.convert(data, numRows),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()