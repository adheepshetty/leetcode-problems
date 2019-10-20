import unittest
class Solution:
    '''
    A self-dividing number is a number that is divisible by every digit it contains.

    For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

    Also, a self-dividing number is not allowed to contain the digit zero.

    Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

    Example 1:
    Input: 
    left = 1, right = 22
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    '''
    def selfDividingNumbers(self, left, right):
        res = []
        for i in range(left, right+1):
            # print("0" in str(i))
            if not "0" in str(i) and all([i%int(v) == 0 for v in str(i)]):
                res.append(i)
        return res

class Test(unittest.TestCase):
    def test_selfDividingNumbers(self):
        left = 1
        right = 22
        expected = [1,2,3,4,5,6,7,8,9,11,12,15,22]
        sol = Solution()
        self.assertEqual(sol.selfDividingNumbers(left, right),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()