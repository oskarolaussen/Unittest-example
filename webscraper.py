from bs4 import BeautifulSoup
import requests
from player import Player

def webscraper():
	list_of_players=[]

	source = requests.get('http://liiga.fi/tilastot/2017-2018/runkosarja/pelaajat/').text
	soup = BeautifulSoup(source, 'lxml')

	table = soup.find('table', class_='tight')
	for player in table.tbody.find_all('tr'):
		name = player.find('td', class_='ta-l').a.text
		columns_list = player.find('td', class_='h-l').find_next_siblings()
		games_played = int(columns_list[0].text)
		goals = int(columns_list[1].text)
		assists = int(columns_list[2].text)
		list_of_players.append(Player(name, games_played, goals, assists))
	return list_of_players

