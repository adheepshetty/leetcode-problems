import unittest
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        sum1 = 0
        sum2 = 0
        for i in range(len(num1)):
            sum1 += num_dic[num1[-i-1]]*(10**i)
            
        for i in range(len(num2)):
            sum2 += num_dic[num2[-i-1]]*(10**i)
            
        return str(sum1*sum2)


class Test(unittest.TestCase):
    def test_multiply(self):
        s1 = "123"
        s2 = "456"
        expected = "56088"
        sol = Solution()
        self.assertEqual(sol.multiply(s1, s2),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()