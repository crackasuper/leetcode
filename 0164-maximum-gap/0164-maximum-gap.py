class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        sortedarr = sorted(nums, reverse = False)
        maxsum = 0
        for i in range(1, len(sortedarr)):
            maxsum = max(maxsum, sortedarr[i] - sortedarr[i -1])

        return maxsum
        