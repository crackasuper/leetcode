class Solution:
    def maximumUniqueSubarray(self, nums):
        dataset = set()
        n = len(nums)
        max_sum = 0
        i = 0
        j = 0
        current_sum = 0
        while j < n:
            current_sum += nums[j]
            while i <= j and nums[j] in dataset:
                current_sum -= nums[i]
                dataset.remove(nums[i])
                i += 1
            max_sum = max(max_sum, current_sum)
            dataset.add(nums[j])
            j += 1
        return max_sum
