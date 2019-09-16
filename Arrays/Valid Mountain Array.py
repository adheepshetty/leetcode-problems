import unittest
class Solution:
    '''
    Given an array A of integers, return true if and only if it is a valid mountain array.

    Recall that A is a mountain array if and only if:

    A.length >= 3
    There exists some i with 0 < i < A.length - 1 such that:
    A[0] < A[1] < ... A[i-1] < A[i]
    A[i] > A[i+1] > ... > A[A.length - 1]
    '''
    def validMountainArray(self, A):
        if len(A) < 3: return False
        
        peak = 0
        index = 0
        
        if A[0] > A[1]: return False
        
        for i in range(0 , len(A) - 1):
            if A[i] > A[i+1]:
                peak = A[i]
                index = i
                break
            if A[i] == A[i+1]:
                return False
        
        for i in range(index+1, len(A)-1):
            if A[i] <= A[i+1]:
                return False
        
        return True


class Test(unittest.TestCase):
    def test_validMountainArray(self):
        data = [0,3,2,1]
        expected = True
        sol = Solution()
        self.assertEqual(sol.validMountainArray(data),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()