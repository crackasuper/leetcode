class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        area = 0
        left = 0
        right = len(height) -1 
        while right > left:
            h = min(height[left], height[right])
            w = right - left
            curr_area = h * w
            area = max(area,curr_area)
            if height[right] > height[left]:
                left += 1

            else:
                right -= 1
        return area