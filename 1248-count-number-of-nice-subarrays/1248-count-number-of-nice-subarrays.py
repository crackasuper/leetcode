class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_count = Counter({0: 1})
      

        result = 0
      
 
        odd_count = 0
      
  
        for num in nums:
            odd_count += num & 1
            result += prefix_count[odd_count - k]
          
            prefix_count[odd_count] += 1
      
        return result


        