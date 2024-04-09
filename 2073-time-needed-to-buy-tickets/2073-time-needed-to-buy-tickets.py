class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i , tick in enumerate(tickets):
            if i <= k:
                ans += min(tick, tickets[k])
            else:
                ans += min(tick, tickets[k] - 1)
        return ans        