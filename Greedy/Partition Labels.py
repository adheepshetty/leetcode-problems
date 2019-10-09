import unittest
# author : Adheep
class Solution:
    '''
    A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

    Example 1:
    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
    '''
    def partitionLabels(self, S) :
        if len(S) == 1: return [1]
        count_labels = {}
        for s in S:
            if s in count_labels:
                count_labels[s] += 1
            else:
                count_labels[s] = 1

        res = []
        prev = 0
        occured = set()
        for i in range(len(S)):
            if S[i] in count_labels:
                count_labels[S[i]] -= 1
                occured.add(S[i])
                 
            if all([count_labels[key] == 0 for key in occured]):
                res.append(S[prev:i+1])
                prev = i+1
        return [len(i) for i in res]


class Test(unittest.TestCase):
    def test_partitionLabels(self):
        data = "ababcbacadefegdehijhklij"
        expected = [9,7,8]
        sol = Solution()
        self.assertEqual(sol.partitionLabels(data),expected)

        

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()