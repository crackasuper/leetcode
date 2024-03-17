class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ""
        for i in range(numRows):
            incr = 2 * (numRows -1)
            for j in range(i, len(s), incr):
                ans += s[j]
                if (i > 0 and i < numRows - 1 and j + incr -2 * i < len(s)):
                    ans += s[j + incr - 2*i]
        return ans        