from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        player_index = 0
        trainer_index = 0
        while trainer_index < len(trainers) and player_index < len(players):
            if (players[player_index] <= trainers[trainer_index]):
                player_index += 1
                trainer_index += 1
            else:
                trainer_index += 1
        return player_index
    
    