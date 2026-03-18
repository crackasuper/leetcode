class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        for j in nums:
            if i < 1 or j > nums[i -1]:
                nums[i] = j
                i += 1
        return i
        