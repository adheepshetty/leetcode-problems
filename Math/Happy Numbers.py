import unittest
class Solution:
    '''
    Write an algorithm to determine if a number is "happy".
    A happy number is a number defined by the following process: 
    Starting with any positive integer, replace the number by the sum of the squares of its digits, 
    and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
    Those numbers for which this process ends in 1 are happy numbers.
    '''
    def isHappy(self, n) :
        Hash = {}
        while n!=1:
            if n in Hash: return False
            else:
                Hash[n] = True
                n = sum([pow(int(c), 2) for c in str(n)])
        return True

class Test(unittest.TestCase):
    def test_isHappy(self):
        num = 7
        res = True
        sol = Solution()
        self.assertEqual(sol.isHappy(num),res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()