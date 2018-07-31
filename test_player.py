import unittest
from player import Player

class TestPlayer(unittest.TestCase):
	
	def setUp(self):
		self.player_1 = Player('Mikael Granlund', 64, 82, 36, 50)
		
	def test_points_per_game(self):
		self.assertEqual(self.player_1.points_per_game(), 1.05)
		
		self.player_1.assists=46
		
		self.assertEqual(self.player_1.points_per_game(), 1.00)
	
	def test_points_pace(self):
		self.assertEqual(self.player_1.points_pace(), 86)
		
		self.player_1.games_played=50
		
		self.assertEqual(self.player_1.points_pace(), 141.04)
		
	def test_goals_pace(self):
		self.assertEqual(self.player_1.goals_pace(), 36)
		
		self.player_1.games_played=50
		
		self.assertEqual(self.player_1.goals_pace(), 59.04)
		
if __name__ == '__main__':
	unittest.main()
	