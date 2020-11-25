from nba_api.stats.endpoints import leaguedashplayershotlocations
from nba_api.stats.endpoints import leaguedashteamshotlocations
import pandas as pd
import collections
import pickle


def get_values(nba):
	"""
	Args:
		nba (dictionary): dictionary of values of all nba players/team
	Return: formated data to only include relevant shots 
	"""
	nba = collections.OrderedDict(nba)
	team_dict = list(nba.values())[2]
	team_values = list(team_dict.values())[2]
	header_dict = list(team_dict.values())[1]
	headers = list(header_dict[1].values())[2]	
	#print(header_dict)
	whole_nba = pd.DataFrame(team_values, columns = headers )
	return whole_nba

def get_all(player):
	"""
	Args:
		player_or_team (boolean): boolean produced from UI to 
		determine if getting information of player or team
	"""
	file_name = "players.p" if player == "Player" else "teams.p"
	endpoint = leaguedashteamshotlocations.LeagueDashTeamShotLocations
	column = "TEAM_NAME"
	if player == "Player":
		endpoint = leaguedashplayershotlocations.LeagueDashPlayerShotLocations
		column = "PLAYER_NAME"

	try:
		whole_nba = pickle.load(open(file_name, "rb"))
	except:
		nba = endpoint(distance_range = "By Zone", season="2019-20")
		nba = nba.get_dict()
		whole_nba = get_values(nba)
		pickle.dump(whole_nba, open(file_name, "wb"))
	return whole_nba[column]



if __name__ == "__main__":

	shot = leaguedashteamshotlocations.LeagueDashTeamShotLocations( distance_range = "By Zone", season="2019-20").get_dict()
	pd.set_option('display.max_columns', 500)

	print(shot)