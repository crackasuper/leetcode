class Solution:
    def checkValidString(self, s: str) -> bool:
        high = 0
        cnt = 0
        for i in s:
            if i == "(":
                cnt += 1
                high += 1
            elif i == ")":
                if cnt > 0:
                    cnt -= 1
                high -= 1
            else:
                if cnt > 0:
                    cnt -= 1
                high += 1
            if high < 0:
                return False
        return cnt == 0

        