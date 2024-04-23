##insertion sort
#counting sort
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        maxHeights = max(heights)
        count = [0] * (maxHeights + 1)
        for i in heights:
            count[i] += 1
        for i in range(1, maxHeights + 1):
            count[i] += count[i -1]
        res_name = [''] * len(names)
        for i in range(len(names) - 1, -1, -1):
           res_name[count[heights[i]] - 1] = names[i]
           count[heights[i]] -= 1
    
        return reversed(res_name)
