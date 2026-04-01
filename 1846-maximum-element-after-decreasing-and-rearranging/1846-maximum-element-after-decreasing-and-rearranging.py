class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        arr.sort()
      
       
        arr[0] = 1
      
        for i in range(1, len(arr)):
           
            difference = max(0, arr[i] - arr[i - 1] - 1)
            arr[i] -= difference
      
        # Return the maximum element in the modified array
        return max(arr)
        