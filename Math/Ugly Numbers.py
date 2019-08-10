import unittest
class Solution(object):
    '''
        Write a program to check whether a given number is an ugly number.

        Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

        '''
        
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0: return False
        while num%5 == 0:
        	num = num//5
        while num%3 == 0:
        	num = num//3
        while num%2 == 0:
        	num = num//2
        return True if num == 1 else False

class Test(unittest.TestCase):
    def test_isUgly(self):
        data = 100
        expected = True
        sol = Solution()
        self.assertEqual(sol.isUgly(data),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()