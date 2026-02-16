class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats = sorted(seats)
        students = sorted(students)

        result = 0

        for idx in range(len(seats)):
            result += abs(students[idx] - seats[idx])
        
        return result
