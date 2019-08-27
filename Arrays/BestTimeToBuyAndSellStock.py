import unittest
class Solution(object):
    '''Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.
    '''
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        
        return max_profit

class Test(unittest.TestCase):
    def test_maxProfit(self):
        data = [7,1,5,3,6,4]
        expected = 5
        sol = Solution()
        self.assertEqual(sol.maxProfit(data),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()