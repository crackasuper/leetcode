class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        result = []
        
        for token in tokens:
            if token in ['+', '/', '-', '*']:
                b = result.pop()
                a = result.pop()

                if token == '+':
                    result.append(a + b)
                elif token =='-':
                    result.append(a - b)
                elif token == '*':
                    result.append(a * b)
                elif token == '/':
                    result.append(int(a/b))
            else:
                result.append(int(token))

        return result[0]
