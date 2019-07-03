import unittest
class Solution(object):
    '''
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    '''
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {  'I':1,
                        'V':5,
                        'X':10,
                        'L':50,
                        'C':100,
                        'D':500,
                        'M':1000}
         
        z = 0
        
        for i in range(0,len(s)-1):
            if dict_roman[s[i]] < dict_roman[s[i+1]]:
                z -= dict_roman[s[i]]
                
            else:
                z += dict_roman[s[i]]
       
        return z + dict_roman[s[-1]]



class Test(unittest.TestCase):
    def test_romanToInt(self):
        data = "IV"
        expected = 4
        sol = Solution()
        self.assertEqual(sol.romanToInt(data),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()