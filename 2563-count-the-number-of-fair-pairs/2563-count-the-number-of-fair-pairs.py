class Solution:
  def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
  
       
    
    nums.sort()  
    n = len(nums)  
    count = 0  
   
    for i in range(n):  
       
        left = lower - nums[i]    
        right = upper - nums[i]   

       
        l_idx = bisect.bisect_left(nums, left, i + 1, n)  
        
        r_idx = bisect.bisect_right(nums, right, i + 1, n)  

        
        count += (r_idx - l_idx)  

    return count  