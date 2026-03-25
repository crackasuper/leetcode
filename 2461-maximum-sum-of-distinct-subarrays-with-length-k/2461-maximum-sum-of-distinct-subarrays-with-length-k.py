class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        element_count = Counter(nums[:k])
        current_sum = sum(nums[:k])
    
        max_sum = current_sum if len(element_count) == k else 0
      

        for i in range(k, len(nums)):

            element_count[nums[i]] += 1
          

            element_count[nums[i - k]] -= 1
          
     
            if element_count[nums[i - k]] == 0:
                element_count.pop(nums[i - k])
    
            current_sum += nums[i] - nums[i - k]
          
           
            if len(element_count) == k:
                max_sum = max(max_sum, current_sum)
      
        return max_sum