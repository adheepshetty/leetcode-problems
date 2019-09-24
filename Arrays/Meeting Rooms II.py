# author: Adheep
import unittest
class Solution:
    '''
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

    Example 1:

    Input: [[0, 30],[5, 10],[15, 20]]
    Output: 2
    '''
    def minMeetingRooms(self, intervals):
        if not intervals: return 0
        used_rooms, start_ptr, end_ptr, start_timings, end_timings = 0, 0, 0, sorted([interval[0] for interval in intervals]), sorted([interval[1] for interval in intervals])
        
        while start_ptr < len(intervals):
            if start_timings[start_ptr] >= end_timings[end_ptr]:
                used_rooms -= 1
                end_ptr += 1
        
            used_rooms += 1
            start_ptr += 1
        return used_rooms


class Test(unittest.TestCase):
    def test_minMeetingRooms(self):
        data = [[0, 30],[5, 10],[15, 20]]
        expected = 2
        sol = Solution()
        self.assertEqual(sol.minMeetingRooms(data),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()