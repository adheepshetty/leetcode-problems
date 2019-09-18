# author: Adheep
import unittest
import heapq
class Solution:
    '''
    We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

    (Here, the distance between two points on a plane is the Euclidean distance.)

    You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
    '''
    def kClosest(self, points, K):
        heap, res = [], []
        heapq.heapify(heap)
        for point in points:
            
            heapq.heappush(heap,(pow(point[0],2) + pow(point[1],2) , point))
        for i in range(K):
            res.append(heapq.heappop(heap)[1])    
        return res

class Test(unittest.TestCase):
    def test_kClosest(self):
        points = [[3,3],[5,-1],[-2,4]]
        K = 2
        expected = [[3,3],[-2,4]]
        sol = Solution()
        self.assertEqual(sol.kClosest(points, K),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()