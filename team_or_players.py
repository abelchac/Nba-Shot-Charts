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
    # print(header_dict)
    whole_nba = pd.DataFrame(team_values, columns=headers)
    return whole_nba


def get_all_nba_info(player_or_team, zone="8ft Range"):
    """
    Args:
            player_or_team (boolean): boolean produced from UI to
            determine if getting information of player or team
    Returns:
            DF of all info in nba
    """
    # print(player_or_team)
    fname = zone.replace(" ", "_")
    file_name = "players_{0}.p".format(
        fname) if player_or_team == "Player" else "teams_{0}.p".format(fname)
    endpoint = leaguedashteamshotlocations.LeagueDashTeamShotLocations
    if player_or_team == "Player":
        endpoint = leaguedashplayershotlocations.LeagueDashPlayerShotLocations
    # print(file_name)
    try:
        whole_nba = pickle.load(open(file_name, "rb"))
    except BaseException:
        nba = endpoint(distance_range=zone, season="2019-20")
        nba = nba.get_dict()
        whole_nba = get_values(nba)
        pickle.dump(whole_nba, open(file_name, "wb"))

    return whole_nba


def get_all(player_or_team):
    """
    Args:
            Args:
            player_or_team (boolean): boolean produced from UI to
            determine if getting information of player or team
    Returns:
            DF of all names/teams
    """
    column = "TEAM_NAME"
    if player_or_team == "Player":
        column = "PLAYER_NAME"
    return get_all_nba_info(player_or_team)[column]


if __name__ == "__main__":

    shot = leaguedashteamshotlocations.LeagueDashTeamShotLocations(
        distance_range="By Zone", season="2019-20").get_dict()
    pd.set_option('display.max_columns', 500)

    print(shot)
