class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        cond = skill[0] + skill[-1]
        i = 0
        j = len(skill) - 1
        ans = 0
        while j > i:
            if skill[i] + skill[j] != cond:
                return -1
            ans += skill[i] * skill[j]
            i,j = i +1, j-1
        return ans