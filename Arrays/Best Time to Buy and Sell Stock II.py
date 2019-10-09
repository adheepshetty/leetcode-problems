import unittest
class Solution:
    def maxProfit(self, prices):
        '''
        Say you have an array for which the ith element is the price of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

        Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

        Example 1:

        Input: [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
        '''
        if prices == sorted(prices, reverse = True) or not prices: return 0
        if prices == sorted(prices): return prices[-1] - prices[0]
        flag = 1
        summ, l = 0, prices[0]
        for i in range(1,len(prices)):
            r = prices[i]
            if prices[i] > l :
                summ += (prices[i] - l)
                l = prices[i]
            if prices[i] < l:
                l = prices[i]
            
        return summ 

class Test(unittest.TestCase):
    def test_maxProfit(self):
        data = [7,1,5,3,6,4]
        expected = 7
        sol = Solution()
        self.assertEqual(sol.maxProfit(data),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()