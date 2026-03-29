class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = []
        for i in range(len(nums)):
            if sum(res) == 0:
                res.append(nums[i])
            else:
                res.append(res[-1] + nums[i])
        return res