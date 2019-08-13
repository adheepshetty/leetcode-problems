from collections import defaultdict 
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        relationship = defaultdict(set)
        for relation in trust:
            relationship[relation[0]].add(relation[1])
        
        possibleTownJudge = None
        
        for i in range(1, N+1):
            if len(relationship[i]) == 0:
                possibleTownJudge = i
            
        for i in range(1, N+1):
            if possibleTownJudge != i:
                if possibleTownJudge not in relationship[i]:
                    return -1
            
        return possibleTownJudge
    
