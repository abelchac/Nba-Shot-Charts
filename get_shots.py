import pickle

def get_shot(player_or_team, spec):
	filename = "players.p" if player_or_team else "teams.p"
	pt_type = "PLAYER_NAME" if player_or_team else "TEAM_NAME"
	whole_nba = pickle.load(open(filename, "rb"))

	drop_list = [pt_type, "TEAM_ID", "FG_PCT"]
	if(pt_type == "PLAYER_NAME"):
		drop_list.append("PLAYER_ID")
		drop_list.append("TEAM_ABBREVIATION")
		drop_list.append("AGE")

	for_average = whole_nba.drop(drop_list, axis=1, inplace = False)


	return [whole_nba.loc[whole_nba[pt_type] == spec], whole_nba.min(), whole_nba.max(), for_average]
