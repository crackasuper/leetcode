class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """

        n = len(arr)

        # First pass: Find how many elements from original array will fit
        # source_index tracks position in original array
        # dest_position tracks position in modified array
        source_index = -1
        dest_position = 0

        while dest_position < n:
            source_index += 1
            # If current element is 0, it takes 2 positions, otherwise 1
            if arr[source_index] == 0:
                dest_position += 2
            else:
                dest_position += 1

        # Start filling from the end of array
        write_position = n - 1

  
        if dest_position == n + 1:
            arr[write_position] = 0
            source_index -= 1
            write_position -= 1

        while write_position >= 0:
            if arr[source_index] == 0:
                # Duplicate the zero
                arr[write_position] = 0
                arr[write_position - 1] = 0
                write_position -= 1
            else:
                # Copy non-zero element
                arr[write_position] = arr[source_index]

            source_index -= 1
            write_position -= 1
        
        
