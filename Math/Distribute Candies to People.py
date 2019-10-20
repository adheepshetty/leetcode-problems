import unittest
class Solution:
    '''
    We distribute some number of candies, to a row of n = num_people people in the following way:

    We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

    Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

    This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

    Return an array (of length num_people and sum candies) that represents the final distribution of candies.

    

    Example 1:

    Input: candies = 7, num_people = 4
    Output: [1,2,3,1]
    Explanation:
    On the first turn, ans[0] += 1, and the array is [1,0,0,0].
    On the second turn, ans[1] += 2, and the array is [1,2,0,0].
    On the third turn, ans[2] += 3, and the array is [1,2,3,0].
    On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
    '''
    def distributeCandies(self, candies, num_people):
        dist = [0]*num_people
        i = 1
        split = 1
        while candies>0:
            dist[(i-1)%num_people] += min(i, candies) 
            candies = candies - i
            i = i+1
        return dist

class Test(unittest.TestCase):
    def test_distributeCandies(self):
        candies = 7
        num_people = 4
        expected = [1,2,3,1]
        sol = Solution()
        self.assertEqual(sol.distributeCandies(candies, num_people),expected)
        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()
