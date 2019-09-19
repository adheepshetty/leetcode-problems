import unittest
class Solution:
    '''
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.'''
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
        return stack == []

class Test(unittest.TestCase):
    def test_isValid(self):
        data = "()"
        expected = True
        sol = Solution()
        self.assertEqual(sol.isValid(data),expected)
        
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()