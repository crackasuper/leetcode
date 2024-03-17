class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if nums is None or len(nums) < 3:
            return False
        minOne = float('inf')
        minTwo = float('inf')
        for i in nums:
            if i > minOne:
                minTwo = min(i, minTwo)
            if i < minOne:
                minOne = i
            if i > minTwo:
                return True
        return False