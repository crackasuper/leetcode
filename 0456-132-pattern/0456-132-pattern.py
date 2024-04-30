class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        min_stack = [nums[0]]

        for i in range(1, len(nums)):
            min_stack.append(min(min_stack[-1], nums[i]))
        for j in range(len(nums) - 1, -1 ,-1):
            if nums[j] > min_stack[j]:
                while stack and stack[-1] <= min_stack[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False


        




        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[k] < nums[j] and nums[k] > nums[i]:
        #                 return True
        # return False