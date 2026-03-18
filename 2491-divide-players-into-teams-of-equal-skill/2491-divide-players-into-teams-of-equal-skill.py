class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """

        skill.sort()
        
        max_value = skill[0] + skill[-1]

        left, right  =  0, len(skill) - 1

        ans = 0

        while right > left:
            if skill[left] + skill[right] != max_value:
                return -1
            ans += (skill[left] * skill[right])

            left += 1
            right -= 1


        return ans
        