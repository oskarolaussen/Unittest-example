class Player:
	
	games_in_full_season = 60
	
	def __init__(self, name, games_played, goals, assists):
		self.name = name
		self.games_played = games_played
		self.goals = goals
		self.assists = assists
	
	def points_per_game(self):
		return round((self.goals + self.assists)/self.games_played, 2)
		
	def points_pace(self):
		return round(((self.goals + self.assists)/self.games_played) * self.games_in_full_season, 2)
		
	def goals_pace(self):
		return round((self.goals / self.games_played) * self.games_in_full_season, 2)
	