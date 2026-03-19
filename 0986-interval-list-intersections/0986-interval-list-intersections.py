class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        

        i = 0  # Pointer for firstList
        j = 0  # Pointer for secondList
        result = []  
      
        while i < len(firstList) and j < len(secondList):
            # Extract start and end points of current intervals
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
      
            intersection_start = max(start1, start2)
            # The intersection ends at the minimum of both end points
            intersection_end = min(end1, end2)
          
           
            if intersection_start <= intersection_end:
                result.append([intersection_start, intersection_end])
          
           
            if end1 < end2:
                i += 1  # Move to next interval in firstList
            else:
                j += 1  # Move to next interval in secondList
      
        return result