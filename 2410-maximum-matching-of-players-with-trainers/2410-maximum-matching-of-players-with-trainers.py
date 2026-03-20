class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """

        ans = 0

        players.sort()
        trainers.sort()

        for i, trainer in enumerate(trainers):
            if players[ans] <= trainer:
                ans += 1
                if ans == len(players):
                     return ans

        return ans
            