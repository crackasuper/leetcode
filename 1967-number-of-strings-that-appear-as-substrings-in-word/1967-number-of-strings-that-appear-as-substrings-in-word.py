class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0

        for i in range(len(patterns)):
            if patterns[i] in word:
                res += 1
        return res
        