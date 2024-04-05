class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        basket = {}
        left = 0

        for right, fruit in enumerate(fruits):
            basket[fruit] = right

            if len(basket) > 2:
                min_index = min(basket.values())
                left = min_index + 1
                del basket[fruits[min_index]]

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
        