class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # result = []
        # n = len(nums)

        # for i in nums:
        #     if nums.count(i) > (n / 3) and i not in result:
        #             result.append(i)

        # return result

        n = len(nums)
        res = []

        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == nums[i]:
                    cnt += 1
            
            if cnt > (n // 3):
                if len(res) == 0 or nums[i] != res[0]:
                    res.append(nums[i])
            
        
            if len(res) == 2:
                if res[0] > res[1]:
                    res[0], res[1] = res[1], res[0]
                break

        return res