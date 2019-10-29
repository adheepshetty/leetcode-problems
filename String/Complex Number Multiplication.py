import re
import unittest
#author: Adheep
class Solution(object):
    '''
    Given two strings representing two complex numbers.

    You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

    Example 1:
    Input: "1+1i", "1+1i"
    Output: "0+2i"
    Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
    Example 2:
    Input: "1+-1i", "1+-1i"
    Output: "0+-2i"
    Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
    '''
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = re.split('[+ i]', a)
        y = re.split('[+ i]', b)
        a_real = int(x[0])
        a_complex = int(x[1])
        b_real = int(y[0])
        b_complex = int(y[1])
        return str(a_real * b_real - a_complex * b_complex) + "+" + str(a_real*b_complex + a_complex*b_real) + "i"


class Test(unittest.TestCase):
    def test_complexNumberMultiply(self):
        i1 = "1+1i"
        i2 = "1+1i"
        expected = "0+2i"
        sol = Solution()
        self.assertEqual(sol.complexNumberMultiply(i1, i2),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()