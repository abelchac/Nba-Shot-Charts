import pickle

def get_shot(player_or_team, spec):
	filename = "players.p" if player_or_team else "teams.p"
	pt_type = "PLAYER_NAME" if player_or_team else "TEAM_NAME"
	whole_nba = pickle.load(open(filename, "rb"))
	return [whole_nba.loc[whole_nba[pt_type] == spec], whole_nba.min(), whole_nba.max()]
