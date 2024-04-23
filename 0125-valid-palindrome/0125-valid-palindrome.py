class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in s:
            if i.isalnum():
                res.append(i.lower())
        ans = "".join(res)
        return ans == ans[::-1]
        

      
       