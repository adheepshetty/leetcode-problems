#author: Adheep
import unittest
class Solution:
    '''
    Implement atoi which converts a string to an integer.

    The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
    Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, 
    and interprets them as a numerical value.
    The string can contain additional characters after those that form the integral number, which are ignored and have no effect 
    on the behavior of this function.
    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either 
    str is empty or it contains only whitespace characters, no conversion is performed.
    If no valid conversion could be performed, a zero value is returned.
    '''
    def myAtoi(self, str):
        str = str.strip()
        if len(str) == 0: return 0
        tmp = "0"
        result = 0
        i = 0
        if str[0] in "+-":
            tmp = str[0]
            i = 1
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        for i in range(i, len(str)):
            if str[i].isdigit():
                tmp += str[i]
                
            else:
                break
        if len(tmp) > 1:
            result = int(tmp)
        if result > MAX_INT > 0:
            return MAX_INT
        elif result < MIN_INT < 0:
            return MIN_INT
        else:
            return result

class Test(unittest.TestCase):
    def test_myAtoi(self):
        s = "42 words 42"
        expected = 42
        sol = Solution()
        self.assertEqual(sol.myAtoi(s),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()