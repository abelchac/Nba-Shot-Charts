from matplotlib.patches import Arc
from matplotlib.patches import Wedge

import matplotlib.pyplot as plt

spotList = []


def draw_circles(size, shot):
    global spotList
    print(shot)
    ax = plt.gca()
    for spots in range( 4 if size == 8 else 6):
        # cur = Arc((0, 0), size * 20 * (spots+1),  size * 20 * (spots+1),linewidth= size*5,
        #             color='black', alpha = .5, fill= 0)
        cur = Wedge((0, 0), size * 10 * (spots+1), 0 , 360, linewidth= 0, width = size * 10,
                   color='green', alpha = shot.iloc[0,4 + 3*spots])
        spotList.append(cur)
        ax.add_patch(cur)

 

    return spotList

def draw_5ft(color = 'black'):
    draw_circles(5)

def remove_fts():
    for els in spotList:
        els.remove()
    spotList.clear()
    
def draw_8ft():
    draw_circles(8)
    
def draw_zones():
    return
