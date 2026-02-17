class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        

        target_x, target_y = target

        player_distance = abs(target_x) + abs(target_y)

        for ghost_x, ghost_y in ghosts:
            ghost_distance = abs(target_x - ghost_x) + abs(target_y - ghost_y)

            if ghost_distance <= player_distance:
                return False
        
        return True
