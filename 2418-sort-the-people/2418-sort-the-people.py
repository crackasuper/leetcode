class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = list(range(len(heights)))
        data.sort(key = lambda i: -heights[i])
        return [names[i] for i in data]
        