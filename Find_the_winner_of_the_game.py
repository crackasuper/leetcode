class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        if n == 1:
            return 1
        
        game_winner = (k + self.findTheWinner(n -1, k)) % n

        if game_winner == 0:
            return n
        else:

            return game_winner
