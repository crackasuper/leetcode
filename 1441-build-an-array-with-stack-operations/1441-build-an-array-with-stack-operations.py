class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        operations = []

        target_index = 0

        for num in range(1, n + 1):
            if target_index == len(target):
                break

            operations.append("Push")

            if num == target[target_index]:
                target_index += 1
            else:
                operations.append("Pop")
        return operations
