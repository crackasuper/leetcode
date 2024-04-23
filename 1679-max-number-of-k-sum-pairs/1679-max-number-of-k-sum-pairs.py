class Solution:
  def maxOperations(self, nums: List[int], k: int) -> int:
    count = collections.Counter(nums)
    return sum(min(count[num], count[k - num])
               for num in count) // 2
    # count = 0
    # left = 0
    # right = len(nums) - 1
    # while right >= left:
    #     if nums[left] + nums[right] == k:
    #         count += 1
    #         nums.remove(nums[left])
    #         nums.remove(nums[right])
    #     right -= 1
    # return count
