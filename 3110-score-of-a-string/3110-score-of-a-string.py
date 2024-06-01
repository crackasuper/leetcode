class Solution:
    def scoreOfString(self, s: str) -> int:
        res = []
        for i in s:
            res.append(ord(i))
        ans = 0
        for i in range(1, len(res)):
            ans += abs(res[i -1] - res[i])
        return ans 

        