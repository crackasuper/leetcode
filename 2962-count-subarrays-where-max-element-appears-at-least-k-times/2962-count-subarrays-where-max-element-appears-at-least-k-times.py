class Solution:
  def countSubarrays(self, nums: List[int], k: int) -> int:
    maxNum = max(nums)
    ans = 0
    count = 0

    l = 0
    for r, num in enumerate(nums):
      if num == maxNum:
        count += 1
    
      while count == k:
        if nums[l] == maxNum:
          count -= 1
        l += 1
    
      ans += l

    return ans