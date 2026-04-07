class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for idx in s:
            if idx == '(':
                stack.append(")")

            elif idx == '{':
                stack.append("}")

            elif idx == '[':
                stack.append("]")
            
            elif not stack or stack.pop() != idx:
                return False

        return not stack
        