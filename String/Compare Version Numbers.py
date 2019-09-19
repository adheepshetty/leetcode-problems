import unittest
class Solution(object):
    '''
    Compare two version numbers version1 and version2.
    If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

    You may assume that the version strings are non-empty and contain only digits and the . character.

    The . character does not represent a decimal point and is used to separate number sequences.

    For instance, 2.5 is not "two and a half" or "half way to version three", 
    it is the fifth second-level revision of the second first-level revision.

    You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 
    and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.
    
    '''
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        val1, val2 = 0, 0
        
        while len(v1) > len(v2): v2.append(0)
        while len(v2) > len(v1): v1.append(0)
        
        for i in range(len(v1)):
            val1 += int(v1[(len(v1)-i-1)])*(10**i)
            val2 += int(v2[(len(v1)-i-1)])*(10**i)
            
        if val1 > val2: return 1
        elif val1 < val2: return -1
        
        return 0

class Test(unittest.TestCase):
    def test_compareVersion(self):
        v1 = "0.1"
        v2 = "1.1"
        expected = -1
        sol = Solution()
        self.assertEqual(sol.compareVersion(v1, v2),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()