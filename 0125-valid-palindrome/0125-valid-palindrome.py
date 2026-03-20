class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left_index = 0
        right_index = len(s) - 1

    
        while left_index < right_index:
            # Skip non-alphanumeric character on the left
            if not s[left_index].isalnum():
                left_index += 1
     
            elif not s[right_index].isalnum():
                right_index -= 1
        
            elif s[left_index].lower() != s[right_index].lower():
                return False
          
            else:
                left_index += 1
                right_index -= 1

        return True
        
