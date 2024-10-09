class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        balance = 0
        for i in range(len(s)):
            if s[i] == "(":
                balance += 1
            else:
                balance += -1
            if balance == -1:
                balance += 1
                res += 1
        return balance + res
                

        