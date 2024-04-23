class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        sorted_s = sorted(s, key = lambda x: int(x[-1]))
        res = [word[:-1] for word in sorted_s]
        return " ".join(res)
       
