class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)

        i, j = 0, 1

        while n > i:
            while n > i and nums[i] % 2 == 0:
                i += 2
            
            while n > j and nums[j] % 2 == 1:
                j += 2
            if n > i:
                nums[i], nums[j] = nums[j], nums[i]
        return nums
        