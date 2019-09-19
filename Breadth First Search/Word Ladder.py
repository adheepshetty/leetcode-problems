# author: Adheep 
# only half of the testcases passed
import unittest
class Solution:
    '''
    Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
    Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length. 
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.
    '''
    def ladderLength(self, beginWord, endWord, wordList):
        def diff_letters(word1, word2):
            return sum(word1[i] != word2[i] for i in range(len(word1)))
        
        if (endWord not in wordList) or ((beginWord in wordList) and (endWord in wordList) and len(wordList) == 2): 
            return 0
        queue = [[0, beginWord]]
        result = []
        if beginWord in wordList: wordList.remove(beginWord)
        while queue:
            for item in queue:
                if endWord in item[1]:
                    result.append(endWord)
                    return len(result)
            queue = sorted(queue , key = lambda x:x[0])
            # print(queue)
            temp = queue.pop(0)[1]
            # print(temp)
            result.append(temp)
            if endWord in result:break
            # print('start')
            for word in wordList:
                if diff_letters(temp, word) == 1:
                    # print(temp, word)
                    # print(wordList)
                    queue.append([diff_letters(word, endWord), word])
                    wordList.remove(word)
                    # print('here',wordList)
            if len(wordList) == 1: 
                single_word = wordList.pop(0)
                queue.append([diff_letters(single_word, endWord), single_word])
            # print('stop')
        
class Test(unittest.TestCase):
    def test_ladderLength(self):
        startWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        expected = 5
        sol = Solution()
        self.assertEqual(sol.ladderLength(startWord, endWord, wordList),expected)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()       