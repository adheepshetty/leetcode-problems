import unittest
class Solution:
    '''There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.'''
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        nums3 = sorted(nums1 + nums2)
        if len(nums3)%2 != 0:
            return float(nums3[int(len(nums3)/2)])
        else:
            return float(((nums3[int(len(nums3)/2)-1]) + nums3[int(len(nums3)/2)])/2)

class Test(unittest.TestCase):
    def test_medianoftwosortedarrays(self):
        nums1 = [1, 3]
        nums2 = [2]
        expected = 2.0
        sol = Solution()
        self.assertEqual(sol.findMedianSortedArrays(nums1, nums2),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()