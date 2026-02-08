class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        counts = Counter(words[0])

        for word in words:
            current_counter = Counter(word)
            for chr in counts:
                counts[chr] = min(counts[chr], current_counter[chr])

        result = []
        for chr in counts:

            for i in range(counts[chr]):
                result.append(chr)

        return result

