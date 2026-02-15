class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        firstRow = "qwertyuiop"
        secondRow = "asdfghjkl"
        thirdRow = "zxcvbnm"

        row_one = set(firstRow)
        row_two, row_three = set(secondRow), set(thirdRow)
        
        result = []

        for word in words:
            current_word = set(word.lower())
            if current_word <= row_one:
                result.append(word)
            elif current_word <= row_two:
                result.append(word)
            elif current_word <= row_three:
                result.append(word)

        return result   