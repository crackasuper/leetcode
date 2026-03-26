class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        frequency_map = Counter()
      
        total_subarrays = 0
        pair_count = 0
  
        left = 0
      

        for num in nums:
        
            pair_count += frequency_map[num]
            frequency_map[num] += 1
          
         
            while pair_count - frequency_map[nums[left]] + 1 >= k:
                frequency_map[nums[left]] -= 1
              
                pair_count -= frequency_map[nums[left]]
                left += 1
          
            if pair_count >= k:
                total_subarrays += left + 1
              
        return total_subarrays
        