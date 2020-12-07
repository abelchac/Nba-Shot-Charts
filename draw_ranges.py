from matplotlib.patches import Arc
from matplotlib.patches import Wedge

import matplotlib.pyplot as plt

spotList = []


def draw_circles(size, shot_data, averages):
    """
    Args:
        size (int): the size of the circles for the shot ranges
        shots (dataframe): the shot chart data of a player or team
    Returns:
        None, but plots the shot ranges
    """
    global spotList
    shot = shot_data   
    ax = plt.gca()
    if(len(shot) == 0):
        return

    for spots in range( 4 if size == 8 else 6):
        edge = Arc((0, 0), size * 20 * (spots+1),  size * 20 * (spots+1),linewidth= 1,
                    color='black', alpha = 1)
        cur_min = averages.get_min()[spots]
        cur_max = averages.get_max()[spots]
        cur_average = averages[spots]
        cur_value = shot.iloc[0,4 + 3*spots]
        set_color = ''
        #print("VALUES")
        print(cur_value, cur_average, cur_min, cur_max)

        if(cur_value >= cur_average):
            set_color = 'green'
            cur_value = min(((cur_value - cur_average )) / (cur_max - cur_average) + .08, .95) 
        else:
            set_color = 'red'
            cur_value = min(1 - ((cur_value - cur_min)) / (cur_average - cur_min) + .08, .95)

        #print(cur_value)
        print(cur_value)
        fill = Wedge((0, 0), size * 10 * (spots+1), 0 , 360, linewidth= 0, width = size * 10,
                   color=set_color, alpha = cur_value)

        spotList.append(edge)
        ax.add_patch(edge)
        spotList.append(fill)
        ax.add_patch(fill)
    return spotList

def remove_fts():
    """
    Args:
        None
    Returns:
        None, but clears the shot chart
    """
    for els in spotList:
        els.remove()
    spotList.clear()
    

def draw_zones():
    return
