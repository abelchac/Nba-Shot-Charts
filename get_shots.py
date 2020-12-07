import pickle
from team_or_players import  *
def get_shot(player_or_team, spec, zone):
	pt_type = "PLAYER_NAME" if player_or_team  == 'Player' else "TEAM_NAME"
	#print(zone)
	whole_nba = get_all_nba_info(player_or_team, zone)
	#print(whole_nba)
	return whole_nba.loc[whole_nba[pt_type] == spec]
