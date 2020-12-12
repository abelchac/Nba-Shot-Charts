import pickle
from team_or_players import *


def get_shot(player_or_team, spec, zone):
    """
    Args:
        player_or_team (boolean): determine the data to pull
        specific_player_team (string): the player or team to evalute
    Returns:
        shots of the player or team that is selected (dataframe)
    """
    pt_type = "PLAYER_NAME" if player_or_team == 'Player' else "TEAM_NAME"
    whole_nba = get_all_nba_info(player_or_team, zone)
    return whole_nba.loc[whole_nba[pt_type] == spec]
