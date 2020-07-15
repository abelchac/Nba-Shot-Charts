from nba_api.stats.endpoints import leaguedashplayershotlocations
from nba_api.stats.endpoints import leaguedashteamshotlocations
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.library.parameters import Season


import pandas as pd
import collections

import pickle


def spot_factory(endpoint, spot, player):
		nba = endpoint( distance_range = spot).get_dict()
		whole_nba = get_values(nba)

# class AllShots:
# 	try:
# 		zonePlayer = pickle.load(open("zonePlayer.p", "rb"))
# 		ft5Player = pickle.load(open("5ftPlayer.p", "rb"))
# 		ft8Player = pickle.load(open("8ftPlayer.p", "rb"))

# 		zoneTeam = pickle.load(open("zoneTeam.p", "rb"))
# 		ft5Player = pickle.load(open("5ftPlayer.p", "rb"))
# 		ft8Player = pickle.load(open("8ftPlayer.p", "rb"))
# 	except :
# 		zonePlayer = spot_factory(shotchartdetail.ShotChartDetail())
# 		ft5Player = spot_factory()
# 		ft8Player =spot_factory()

# 		zoneTeam = spot_factory()
# 		ft5Player = spot_factory()
# 		ft8Player = spot_factory()



# 		pickle.dump()



def get_values(nba):
	nba = collections.OrderedDict(nba)
	team_dict = list(nba.values())[2]
	team_values = list(team_dict.values())[2]
	header_dict = list(team_dict.values())[1]
	headers = list(header_dict[1].values())[2]	
	print(header_dict)
	whole_nba = pd.DataFrame(team_values, columns = headers )
	return whole_nba




def get_all_players():
	try:
		whole_nba = pickle.load(open("players.p", "rb"))
	except:
		nba = leaguedashplayershotlocations.LeagueDashPlayerShotLocations( distance_range = "By Zone").get_dict()
		whole_nba = get_values(nba)
		pickle.dump(whole_nba, open("players.p", "wb"))
	return whole_nba["PLAYER_NAME"]

def get_all_teams():
	try:
		whole_nba = pickle.load(open("teams.p", "rb"))
	except:
		nba = leaguedashteamshotlocations.LeagueDashTeamShotLocations( distance_range = "By Zone").get_dict()
		whole_nba = get_values(nba)
		pickle.dump(whole_nba, open("teams.p", "wb"))
	return whole_nba["TEAM_NAME"]

	
def get_all(player):
	if(player == "Player"):
		return get_all_players()
	else:
		return get_all_teams()

shot = shotchartdetail.ShotChartDetail(player_id = 0, team_id = 1610612755, season_nullable= Season.default).get_data_frames()[0]
pd.set_option('display.max_columns', 500)

print(shot)