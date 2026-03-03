class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        return sum(sorted(piles)[len(piles) // 3::2])
     
        