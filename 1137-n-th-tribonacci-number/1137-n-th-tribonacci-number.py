class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [0, 1,1]
        if n < 3:
            return trib[n]
        for i in range(3, n + 1):
            trib[0], trib[1], trib[2] = trib[1], trib[2], sum(trib)
        return trib[-1]
        