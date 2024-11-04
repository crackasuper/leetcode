class Solution:
    def compressedString(self, word: str) -> str:
        comp = []

        n = len(word)

        i = 0
        
        while n > i:
            char = word[i]
            count  = 0

            while n > i and word[i] == char and 9 > count:
                count += 1
                i += 1
            comp.append(str(count))
            comp.append(char)
        return ''.join(comp)

        