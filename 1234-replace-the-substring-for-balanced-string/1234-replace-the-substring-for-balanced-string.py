class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_count = Counter(s)
        n = len(s)
        target_count = n // 4 
       
        if all(count <= target_count for count in char_count.values()):
            return 0
      
        min_window_size = n  # Initialize minimum window size to string length
        left = 0  # Left pointer of sliding window
      
       
        for right, char in enumerate(s):
           
            char_count[char] -= 1
          
            while left <= right and all(count <= target_count for count in char_count.values()):
               
                min_window_size = min(min_window_size, right - left + 1)
               
                char_count[s[left]] += 1
                left += 1
      
        return min_window_size
        