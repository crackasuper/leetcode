class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # str2 = ""
        # for i in range(len(typed)):
        #     if typed[i] not in str2:
        #         str2 += typed[i]
        #     elif typed[i] == str2[-1]:
        #         pass
        # return name == str2
        i = 0
        for j, k in enumerate(typed):
            if len(name) > i and name[i] == k:
                i += 1
            elif j == 0 or k != typed[j -1]:
                return False
        return i == len(name)
        