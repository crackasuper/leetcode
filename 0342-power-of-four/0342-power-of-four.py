class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif 1 > n:
            return False
        else:
            return self.isPowerOfFour(n / 4)
        