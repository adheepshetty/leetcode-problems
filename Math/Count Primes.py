import unittest
class Solution:
    '''
    Count the number of prime numbers less than a non-negative number, n.
    '''
    def countPrimes(self, n: int) -> int:
        if n<3: return 0
        is_prime = [True] * (n+1)
        is_prime[1] = False 
        is_prime[0] = False
        for i in range(2 , int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i, n+1, i):
                    is_prime[j] = False
                    
        res = {x for x in range(2, n) if is_prime[x]}
        
        if res: return len(res)
        else: return 0
        
class Test(unittest.TestCase):
    def test_countPrimes(self):
        data = 10
        expected = 4
        sol = Solution()
        self.assertEqual(sol.countPrimes(data),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()