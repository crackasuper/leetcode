class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if 1 >= k:
            return 0
        l = ans = 0
        curr = 1
        for r in range(len(nums)):
            curr *= nums[r]
            while curr >= k:
                curr //= nums[l]
                l += 1
            ans += r - l + 1
        return ans
        