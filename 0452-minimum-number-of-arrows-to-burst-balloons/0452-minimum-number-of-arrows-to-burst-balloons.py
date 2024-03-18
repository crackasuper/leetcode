class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = len(points)
        prv = points[0]

        for i in range(1, len(points)):
            curr = points[i]
            if curr[0] <= prv[1]:
                res -= 1
                prv = [curr[0], min(curr[1], prv[1])]
            else:
                prv = curr
        return res
        