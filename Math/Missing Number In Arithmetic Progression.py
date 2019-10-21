import unittest
class Solution(object):
    '''
    In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

    Then, a value from arr was removed that was not the first or last value in the array.

    Return the removed value.

    

    Example 1:

    Input: arr = [5,7,11,13]
    Output: 9
    Explanation: The previous array was [5,7,9,11,13].
    Example 2:

    Input: arr = [15,13,12]
    Output: 14
    Explanation: The previous array was [15,14,13,12].
    '''
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d = (arr[-1] - arr[0])/len(arr)
        
        for i in range(1,len(arr)):
            if d != arr[i] - arr[i-1]:
                return arr[i-1] + d
        return 0
            
class Test(unittest.TestCase):
    def test_missingNumber(self):
        data = [5,7,11,13]
        expected = 9
        sol = Solution()
        self.assertEqual(sol.missingNumber(data),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()