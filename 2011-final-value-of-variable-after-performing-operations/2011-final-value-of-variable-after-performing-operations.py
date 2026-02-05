class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        X = 0

        for opt in operations:
            if opt =='++X' or opt == 'X++':
                X += 1
            elif opt == '--X' or opt == 'X--':
                X -= 1

        return X