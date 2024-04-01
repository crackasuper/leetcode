class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.rstrip(" ")
        ans = res.split()
        return len(ans[-1])
        