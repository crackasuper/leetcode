class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result = []

        # for value in arr2:
        #     while value in arr1:
        #         result.append(value)
        #         arr1.remove(value)

        # for i in range(len(arr1)):
        #     for j in range(1, len(arr1)):
        #         if arr1[i] > arr1[j]:
        #             arr1[i], arr1[j] = arr1[j], arr1[i]

        # if sorted(arr1):

        #     for i in arr1:
        #         result.append(i)


           
        count = [0] * 1001

        for a in arr1:
             count[a] += 1

        for a in arr2:
            while count[a] > 0:
                result.append(a)
                count[a] -= 1

        for num in range(1001):
            for _ in range(count[num]):
                result.append(num)

        return result

        
        