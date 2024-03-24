class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        case = len(nums) + 1
        res = 0
        for i in range(case):
            if i not in nums:
                res = i
        return res

        