from team_or_players import  *

class PlayerTeamAverage:
    def __init__(self):

        self.cur_shot = "5ft Range"
        self.shot_5ft = []
        self.shot_8ft = []
        self.shot_5ft_max = []
        self.shot_5ft_min = []
        self.shot_8ft_max = []
        self.shot_8ft_min = []

        self.shot_team_avg_5ft_attempts = []
        self.shot_team_avg_8ft_attempts = []
        self.shot_player_avg_5ft_attempts = []
        self.shot_player_avg_8ft_attempts = []

        team_info_8ft = get_all_nba_info("Team", "8ft Range")
        team_info_5ft = get_all_nba_info("Team", "5ft Range")
        player_info_8ft = get_all_nba_info("Player", "8ft Range")
        player_info_5ft = get_all_nba_info("Player", "5ft Range")

        drop_list_team = ["TEAM_NAME", "TEAM_ID", "FG_PCT" ,"TEAM_ID"]
        drop_list_player = ["PLAYER_ID","TEAM_ID", "FG_PCT" ,"TEAM_ID", "TEAM_ABBREVIATION"]
        team_info_8ft = team_info_8ft.drop(drop_list_team, axis=1, inplace = False)
        team_info_5ft = team_info_5ft.drop(drop_list_team, axis=1, inplace = False)
        player_info_5ft = player_info_5ft.drop(drop_list_player, axis=1, inplace = False)
        player_info_8ft = player_info_8ft.drop(drop_list_player, axis=1, inplace = False)


        for spots in range(6):
            field_goal_makes_team_5ft = team_info_5ft.iloc[:, spots*2].sum()
            field_goal_attempts_team_5ft =  team_info_5ft.iloc[:, spots*2 + 1].sum()
            self.shot_team_avg_5ft_attempts.append(team_info_5ft.iloc[:, spots*2 + 1].sum()
                                                /len(team_info_5ft.iloc[:, spots*2 + 1]))
            self.shot_player_avg_5ft_attempts.append(player_info_5ft.iloc[:, spots*2 + 1].sum()
                                                /len(player_info_5ft.iloc[:, spots*2 + 1]))
            # self.shot_team_avg_attempts.append()
            self.shot_5ft.append(field_goal_makes_team_5ft / (field_goal_attempts_team_5ft))
            divide = team_info_5ft.iloc[:, spots*2] / team_info_5ft.iloc[:, spots*2 + 1]
            self.shot_5ft_max.append(divide.max())
            self.shot_5ft_min.append(divide.min())

        for spots in range(4):
            field_goal_makes_team_8ft = team_info_8ft.iloc[:, spots*2].sum()
            field_goal_attempts_team_8ft =  team_info_8ft.iloc[:, spots*2 + 1].sum()

            self.shot_8ft.append(field_goal_makes_team_8ft / (field_goal_attempts_team_8ft))
            self.shot_player_avg_8ft_attempts.append(team_info_8ft.iloc[:, spots*2 + 1].sum()
                                                /len(team_info_8ft.iloc[:, spots*2 + 1]))
            self.shot_player_avg_8ft_attempts.append(player_info_8ft.iloc[:, spots*2 + 1].sum()
                                                /len(player_info_8ft.iloc[:, spots*2 + 1]))
            divide = team_info_8ft.iloc[:, spots*2] / team_info_8ft.iloc[:, spots*2 + 1]
            self.shot_8ft_max.append(divide.max())
            self.shot_8ft_min.append(divide.min())
    
    def __getitem__(self, position):
        cur_shot_array = self.shot_5ft if self.cur_shot  == "5ft Range" else self.shot_8ft
        return cur_shot_array[position]

    def get_min(self):
       return self.shot_8ft_min if self.cur_shot == "8ft Range" else self.shot_5ft_min

    def get_max(self):
        return self.shot_8ft_max if self.cur_shot == "8ft Range" else self.shot_5ft_max


 
kk = PlayerTeamAverage()

print(kk.shot_5ft)