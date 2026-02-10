class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data_dic = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in data_dic:
                return [data_dic[val] , i]
            data_dic[num] = i
        