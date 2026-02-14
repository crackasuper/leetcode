class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse_code = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."
        ]

        transformation = set()

        for word in words:
            morse_transformation = ''.join(morse_code[ord(char) - ord('a')] for char in word)

            transformation.add(morse_transformation)
    
        return len(transformation)
