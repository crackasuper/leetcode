class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = collections.Counter(nums)
        return sum(min(count[num], count[k - num])
               for num in count) // 2
        