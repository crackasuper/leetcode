class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        steps = len(t)

        targeted_index = 0
        
        
        for char in s:
            if targeted_index < steps and char == t[targeted_index]:

                targeted_index += 1

                
        return steps - targeted_index