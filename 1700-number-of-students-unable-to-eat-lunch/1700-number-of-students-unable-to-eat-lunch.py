class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt  = Counter(students)
        for i in sandwiches:
            if cnt[i] > 0:
                cnt[i] -= 1
                res -= 1
            else:
                return res
        return res