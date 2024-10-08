class Solution:
    def minSwaps(self, s: str) -> int:
        unmatched = 0

        for i in s:
            if i == '[':
                unmatched += 1
            elif unmatched > 0:
                unmatched -= 1
        return (unmatched + 1) // 2

        
        