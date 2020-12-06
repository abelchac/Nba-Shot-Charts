from team_or_players import  *

class PlayerTeamAverage:
  def __init__(self):

    self.cur_shot = "5ft Range"
    self.shot_5ft = []
    self.shot_8ft = []
    team_info = get_all_nba_info("TEAM")

    drop_list_player = ["TEAM_NAME", "TEAM_ID", "FG_PCT" ,"TEAM_ID"]
    team_info = team_info.drop(drop_list_player, axis=1, inplace = False)
    print(team_info)
    print(team_info.iloc[0, [0]].sum() /team_info.iloc[0, [ 1]].sum())
    for spots in range(6):
        field_goal_makes_player_5ft = team_info.iloc[0, [spots*2]].sum()
        field_goal_attempts_player_5ft =  team_info.iloc[0, [spots*2 + 1]].sum()
        self.shot_5ft.append(field_goal_makes_player_5ft / (field_goal_attempts_player_5ft))

    for spots in range(4):
        field_goal_makes_player_8ft = team_info.iloc[0, [spots*2]].sum()
        field_goal_attempts_player_8ft =  team_info.iloc[0, [spots*2 + 1]].sum()
        self.shot_8ft.append(field_goal_makes_player_8ft / (field_goal_attempts_player_8ft))
    
  def __getitem__(self, position):
    cur_shot_array = self.shot_5ft if self.cur_shot  == "5ft Range" else self.shot_8ft
    return cur_shot_array[position]
