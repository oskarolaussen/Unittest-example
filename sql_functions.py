def insert_player(player, cursor, connection):
	with connection:
		cursor.execute("INSERT INTO players VALUES (:name, :games, :goals, :assists, :ppg, :ppace, :gpace)" , 
		{'name': player.name, 'games': player.games_played, 'goals': player.goals, 'assists': player.assists, 'ppg': player.points_per_game(), 'ppace':player.points_pace(), 'gpace': player.goals_pace()})
	return
	
def update_player(player, cursor, connection):
	with connection:
		cursor.execute("UPDATE players SET games = :games, goals = :goals, assists = :assists, ppg = :ppg, ppace = :ppace, gpace = :gpace WHERE name=:name" , 
		{'name': player.name, 'games': player.games_played, 'goals': player.goals, 'assists': player.assists, 'ppg': player.points_per_game(), 'ppace':player.points_pace(), 'gpace': player.goals_pace()})
	return
	
def get_player(fullname, cursor):
	fullname = str(fullname)
	cursor.execute("SELECT * FROM players WHERE name = :name", {'name': fullname})
	return cursor.fetchone()