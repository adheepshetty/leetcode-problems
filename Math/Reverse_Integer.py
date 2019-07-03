import unittest
class Solution:
    '''
    Given a 32-bit signed integer, reverse digits of an integer.
    '''
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if -2**31 <= x <= (2**31)-1:
            while x%10 == 0:
                x = x/10
        # print(str(int(x))[::-1])
            if str(x)[0] == '-':
                x = x * -1
                if -2**31<= int('-'+str(int(x))[::-1]) <= 2**31-1:
                    return int('-'+str(int(x))[::-1])
        else:
            return 0
        if -2**31 <= int(str(int(x))[::-1]) <= 2**31-1:
            return int(str(int(x))[::-1])
        else:
            return 0

class Test(unittest.TestCase):
    def test_reverse(self):
        data = 123
        expected = 321
        sol = Solution()
        self.assertEqual(sol.reverse(data),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()