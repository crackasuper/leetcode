class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        cur_sum = 0
        while numbers[left] + numbers[right] != target:
                cur_sum = numbers[left] + numbers[right]
                if cur_sum < target:
                      left += 1
                else:
                    right -= 1
        return [left + 1,right + 1]