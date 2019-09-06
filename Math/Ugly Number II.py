import unittest
class Solution(object):
    '''
    Write a program to find the n-th ugly number.
    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
    '''
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            ugly2, ugly3,ugly5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
            umin = min(ugly2, ugly3, ugly5)
            if umin == ugly2:
                i2 += 1
            if umin == ugly3:
                i3 +=1
            if umin == ugly5:
                i5 +=1
            ugly.append(umin)
            n -=1
        return ugly[-1]

class Test(unittest.TestCase):
    def test_nthUglyNumber(self):
        data = 10
        expected = 12
        sol = Solution()
        self.assertEqual(sol.nthUglyNumber(data),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()
