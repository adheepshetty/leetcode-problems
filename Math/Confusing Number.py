import unittest
class Solution(object):
    '''
    iven a number N, return true if and only if it is a confusing number, which satisfies the following condition:

    We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

    

    Example 1:
    6 -> 9
    Input: 6
    Output: true
    Explanation: 
    We get 9 after rotating 6, 9 is a valid number and 9!=6.
    '''
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        no_change = ['0','1','8']
        valid = ['0', '1', '6', '8', '9']
        start = str(N)[0]
        print([False if ((i in no_change) and (start == i)) else True for i in str(N)])
        if any([False if ((i in no_change) and (start == i)) else True for i in str(N)]):
            # print('gerer')
            return all([True if i in valid else False for i in str(N)])
        return False
    
class Test(unittest.TestCase):
    def test_confusingNumber(self):
        data = 89
        expected = True
        sol = Solution()
        self.assertEqual(sol.confusingNumber(data),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()