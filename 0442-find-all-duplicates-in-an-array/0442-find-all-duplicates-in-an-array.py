class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            a = nums[abs(num) -1]
            if a < 0:
                res.append(abs(num))
            else:
                nums[abs(num) -1] *= -1
        return res