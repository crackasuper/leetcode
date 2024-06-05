class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if sum(res) == 0:
                res.append(nums[i])
            else:
                res.append(res[-1] + nums[i])
        return res
        