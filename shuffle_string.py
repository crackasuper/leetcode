class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        n = len(s)

        result = ['u'] * n
        j = 0
        for i in indices:
            result[i] = s[j]
            j += 1
        return ''.join(result)

        
