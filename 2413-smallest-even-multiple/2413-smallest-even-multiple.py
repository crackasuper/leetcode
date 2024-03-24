class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        res = n
        if n % 2 == 0:
            res = min(res, n * 2)
        else:
            res = n * 2
        return res
        