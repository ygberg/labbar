class SteamUser():
    def __init__(self,username:str, games:list, played_hours:int = 0):
        self.username = username
        self.games = games
        self.played_hours = played_hours
    
    def play(self,game, hours):
        self.hours = hours
        self.game = game
        if game in self.games: 
            self.played_hours += hours
            return f'{self.username} is playing {game}'
        else:
            return f'{game} is not in library'
    
    def buy_game(self,game):
        self.game = game
        if game in self.games:
            return f'you allready own {game}'
        else:
            self.games.append(game)
            return f'{game} have been bought and added to your library'

    def stats(self):
        return f'{self.username} has {len(self.games)} and has played {self.played_hours}'


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.stats())

