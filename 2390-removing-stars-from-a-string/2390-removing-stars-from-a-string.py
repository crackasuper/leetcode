class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []

        for idx in range(len(s)):
            
            if s[idx] == '*':
                stack.pop()
            
            else:
                stack.append(s[idx])

        return "".join(stack)