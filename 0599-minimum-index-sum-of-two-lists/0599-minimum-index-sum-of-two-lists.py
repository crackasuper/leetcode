class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        result = []
        mini_sum = float('inf')

        indexed_word = {word: i for i, word in enumerate(list2)}

        for i, word in enumerate(list1):
            if word in indexed_word:
                current_sum =  i + indexed_word[word]

                if mini_sum > current_sum:
                    mini_sum = current_sum
                    result = [word]
                elif current_sum == mini_sum:
                    result.append(word)

        # for word in list1:
            

        #     if word in list2:
        #         current_sum = list1.index(word) + list2.index(word)
        #         if len(result) >= 1:

        #             prev_sum = list1.index(result[0]) + list2.index(result[0])
        #             if prev_sum > current_sum:
        #                 result[0] = word
        #         result.append(word)
        return result