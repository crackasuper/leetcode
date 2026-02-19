class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        number_of_pairs = 0

        # left, right = 0, len(nums) - 1

        # while left < right:
        #     if nums[left] == nums[right] and (left * right) % k == 0:
        #         number_of_pairs += 1

        #         left += 1
        #         right -= 1

        #     left += 1
        #     right -= 1
        

        # for idx in range(len(nums)):
        #     for jdx in range(1, len(nums)):
        #         if nums[idx] == nums[jdx] and (idx * jdx) % k == 0:
        #             number_of_pairs += 1

        for j in range(1, len(nums)):

            for i in range(j):

                if nums[i] == nums[j] and (i * j) % k == 0:

                    number_of_pairs += 1

        return number_of_pairs
