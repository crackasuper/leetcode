class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def is_valid_palindrome(left, right):

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                    
                return is_valid_palindrome(left, right - 1) or is_valid_palindrome(left + 1, right)
            
              
            left += 1
            right -= 1
        
           
        return True
            
        