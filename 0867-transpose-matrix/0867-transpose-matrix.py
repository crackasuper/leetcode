class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # for rows in range(len(matrix)):
        #     for columns in range(1, len(matrix)):
        #         matrix[rows][columns] = matrix[columns][rows]
        matrix = list(zip(*matrix))
        return matrix