class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if 1 > num:
            return False
        
        left, right = 1,  num

        while right >= left:
            mid = (left + right) // 2
            square = mid ** 2

            if square == num:
                return True
            elif num > square:
                left += 1
            
            else:
                right = mid - 1
        return False
