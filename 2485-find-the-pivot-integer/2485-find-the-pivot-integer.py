class Solution:
    def pivotInteger(self, n: int) -> int:
        a = (n * n +n) // 2
        x = int(math.sqrt(a))
        return x if x * x == a else -1
        