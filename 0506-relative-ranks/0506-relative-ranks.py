class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        n = len(score)
        res = [''] * n
        indices = list(range(n))
        indices.sort(key = lambda x: score[x], reverse = True)
        for i in range(n):
            if i == 0:
                res[indices[0]] = 'Gold Medal'
            elif i == 1:
                res[indices[1]] = 'Silver Medal'
            elif i == 2:
                res[indices[2]] = 'Bronze Medal'
            else:
                res[indices[i]] = str(i + 1)
       
        return res

        