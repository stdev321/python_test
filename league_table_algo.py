class LeagueTable:
    def __init__(self, players):
        self.players = players
        self.scores = {player: 0 for player in players}
        self.games_played = {player: 0 for player in players}

    def record_result(self, player, score):
        self.scores[player] += score
        self.games_played[player] += 1

    def player_rank(self, rank):
        print(self.scores)
        print(self.games_played)
        sorted_players = sorted(
            self.players,
            key=lambda x: (
                self.scores[x],
                -self.games_played[x],
                -self.players.index(x),
            ),
            reverse=True,
        )
        
        print(sorted_players)
        return sorted_players[rank - 1]


table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 6)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)

print(table.player_rank(1))