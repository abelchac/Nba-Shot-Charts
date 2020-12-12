from team_or_players import *


class PlayerTeamAverage:
    def __init__(self):
        """
        Args:
            None
        Returns:
            None, rather evaluates all data
            that is needed for averages, minimum and
            maximum shot attempts and percentages.
        """
        self.cur_shot = "5ft Range"
        self.cur_selection = "Player"
        self.shot_5ft_avg = []
        self.shot_8ft_avg = []
        self.shot_5ft_max = []
        self.shot_5ft_min = []
        self.shot_8ft_max = []
        self.shot_8ft_min = []
        self.attempts_max_player = 0
        self.attempts_max_team = 0
        self.shot_team_avg_5ft_attempts = []
        self.shot_team_avg_8ft_attempts = []
        self.shot_player_avg_5ft_attempts = []
        self.shot_player_avg_8ft_attempts = []

        team_info_8ft = get_all_nba_info("Team", "8ft Range")
        team_info_5ft = get_all_nba_info("Team", "5ft Range")
        player_info_8ft = get_all_nba_info("Player", "8ft Range")
        player_info_5ft = get_all_nba_info("Player", "5ft Range")

        drop_list_team = ["TEAM_NAME", "TEAM_ID", "FG_PCT", "TEAM_ID"]
        drop_list_player = [
            "PLAYER_ID",
            "TEAM_ID",
            "FG_PCT",
            "TEAM_ID",
            "TEAM_ABBREVIATION"]
        team_info_8ft = team_info_8ft.drop(
            drop_list_team, axis=1, inplace=False)
        team_info_5ft = team_info_5ft.drop(
            drop_list_team, axis=1, inplace=False)
        player_info_5ft = player_info_5ft.drop(
            drop_list_player, axis=1, inplace=False)
        player_info_8ft = player_info_8ft.drop(
            drop_list_player, axis=1, inplace=False)

        for spots in range(6):
            field_goal_makes_team_5ft = (
                team_info_5ft.iloc[:, spots * 2].sum())
            field_goal_attempts_team_5ft = (
                team_info_5ft.iloc[:, spots * 2 + 1].sum())
            self.shot_team_avg_5ft_attempts.append(
                team_info_5ft.iloc[:, spots * 2 + 1].sum()
                / len(team_info_5ft.iloc[:, spots * 2 + 1]))
            self.shot_player_avg_5ft_attempts.append(
                player_info_5ft.iloc[:, spots * 2 + 1].sum()
                / len(player_info_5ft.iloc[:, spots * 2 + 1]))
            # self.shot_team_avg_attempts.append()
            self.shot_5ft_avg.append(
                field_goal_makes_team_5ft /
                (field_goal_attempts_team_5ft))
            divide = team_info_5ft.iloc[:, spots * 2] / \
                team_info_5ft.iloc[:, spots * 2 + 1]
            self.shot_5ft_max.append(divide.max())
            self.shot_5ft_min.append(divide.min())

        for spots in range(4):
            field_goal_makes_team_8ft = (
                                team_info_8ft.iloc[:, spots * 2].sum())

            field_goal_attempts_team_8ft = (
                        team_info_8ft.iloc[:, spots * 2 + 1].sum())

            self.attempts_max_team = max(self.attempts_max_team, max(
                team_info_8ft.iloc[:, spots * 2 + 1]))
            self.attempts_max_player = max(self.attempts_max_player, max(
                player_info_8ft.iloc[:, spots * 2 + 1]))

            self.shot_8ft_avg.append(
                field_goal_makes_team_8ft /
                (field_goal_attempts_team_8ft))
            self.shot_team_avg_8ft_attempts.append(
                team_info_8ft.iloc[:, spots * 2 + 1].sum()
                / len(team_info_8ft.iloc[:, spots * 2 + 1]))
            self.shot_player_avg_8ft_attempts.append(
                player_info_8ft.iloc[:, spots * 2 + 1].sum()
                / len(player_info_8ft.iloc[:, spots * 2 + 1]))
            divide = team_info_8ft.iloc[:, spots * 2] / \
                team_info_8ft.iloc[:, spots * 2 + 1]
            self.shot_8ft_max.append(divide.max())
            self.shot_8ft_min.append(divide.min())

    def __getitem__(self, position):
        """
        Args:
            position(integer): the position of
            the data that is wanted from one of the
            shot chart arrays
        Returns:
            The average at the specified index
        """
        cur_shot_array = (self.shot_5ft_avg
                          if self.cur_shot == "5ft Range"
                          else self.shot_8ft_avg)
        return cur_shot_array[position]

    def get_min_avg(self):
        """
        Args:
            NONE
        Returns:
            The array of the minimum averages at each range
        """
        return min(
            self.shot_8ft_min) if self.cur_shot == "8ft Range" else min(
            self.shot_5ft_min)

    def get_max_attempts(self):
        """
        Args:
            NONE
        Returns:
            The overall maximum attempts at each range
        """
        cur_max = (self.attempts_max_player
                   if self.cur_selection == "Player"
                   else self.attempts_max_team)
        return cur_max

    def get_min_list(self):
        """
        Args:
            NONE
        Returns:
            The array of the minimum attempts at each range
        """
        cur_min = (self.shot_8ft_min
                   if self.cur_shot == "8ft Range"
                   else self.shot_5ft_min)
        return cur_min

    def get_max_list(self):
        """
        Args:
            NONE
        Returns:
            The array of the maximum attempts at each range
        """
        cur_max = (self.shot_8ft_max if
                   self.cur_shot == "8ft Range"
                   else self.shot_5ft_max)
        return cur_max
