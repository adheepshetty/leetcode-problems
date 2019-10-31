import unittest
class Solution(object):
    '''
    Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

    Note that it is the kth smallest element in the sorted order, not the kth distinct element.

    Example:

    matrix = [
    [ 1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
    ],
    k = 8,

    return 13.
    '''

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        res = []
        for ele in matrix:
            res += ele
        return sorted(res)[k-1]


class Test(unittest.TestCase):
    def test_kthSmallest(self):    
        actual = [[ 1,  5,  9], [10, 11, 13], [12, 13, 15]]
        k = 8
        expected = 13
        sol = Solution()
        self.assertEqual(sol.kthSmallest(actual, k), expected)

if __name__ == '__main__':
    sol = Solution()
    print(sol.__doc__)
    unittest.main()
    