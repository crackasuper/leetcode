class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        data = set()
        l = 0
        for r in range(len(nums)):
            if r -l > k:
                data.remove(nums[l])
                l += 1

            if nums[r] in data:
                return True
            data.add(nums[r])
        return False