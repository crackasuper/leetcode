class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

    
        char_count = Counter(s1)
   
        chars_needed = len(char_count)
       
        window_size = len(s1)
      
     
        for index, char in enumerate(s2):
          
            char_count[char] -= 1
           
            if char_count[char] == 0:
                chars_needed -= 1
          
           
            if index >= window_size:
                left_char = s2[index - window_size]
          
                char_count[left_char] += 1
               
                if char_count[left_char] == 1:
                    chars_needed += 1
          
       
            if chars_needed == 0:
                return True
      
       
        return False


        