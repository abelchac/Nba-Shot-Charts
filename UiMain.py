import tkinter
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure
import numpy as np
from draw_court import draw_court
import matplotlib.pyplot as plt
from draw_ranges import *
from team_or_players import *
from get_shots import *
from playerTeamClass import PlayerTeamAverage
import seaborn as sns

root = None
listbox = None
ftlist = []
lastzone = ""
last_PT_Type = ""
last_player_team = ""
labels_5ft = [
    "LESS THAN 5FT",
    "5-9 FT.",
    "10-14 FT.",
    "15-19 FT.",
    "20-24 FT.",
    "25-29 FT."]
labels_8ft = ["LESS THAN 8FT.", " 8-16 FT.", "16-24 FT.", "24+ FT."]
after_queue = []


def close_window():
    """
    Args:
      None
    Returns:
      NONE, quits and destroys the tkinter window
      cancels any queued up jobs
    """
    for jobs in after_queue:
        root.after_cancel(jobs)
    root.quit()
    root.destroy()


def list_select():
    """
    Args:
      None
    Returns:
      The currently selected player/team from a
      list in tkinter
    """
    global listbox

    cur = listbox.curselection()
    if(len(cur) == 0):
        return ""
    else:
        return listbox.get(cur[0])


def update():
    """
    Args:
      None
    Returns:
      None, but will update the shot chart to
      reflect the currently selected player
    """
    if(len(after_queue) > 0):
        after_queue.pop()
    global lastzone
    global last_PT_Type
    global last_player_team

    selectedPlayerTeam = list_select()

    zoneClickString = ZoneClikced.get()
    teamOrPlayer = playerOrTeamClicked.get()

    if(last_PT_Type != teamOrPlayer):
        listbox.delete(0, END)
        # print("hee")
        listFill = get_all(teamOrPlayer)
        for item in listFill:
            listbox.insert(END, item)
        listbox.activate(0)
        scrollbar = Scrollbar(frame1)
        listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=3, column=3, sticky='ns', rowspan=3)
        scrollbar.config(command=listbox.yview)
        scrollbar.size()
        last_PT_Type = teamOrPlayer

    if(selectedPlayerTeam == ""):
        selectedPlayerTeam = last_player_team

    if(ZoneClikced.get() == lastzone
       and (selectedPlayerTeam == last_player_team)):
        after_queue.append(root.after(100, update))
        return

    remove_fts()
    draw_court()

    if(len(selectedPlayerTeam) != 0 and zoneClickString != "By Zone"):
        shot_data = get_shot(teamOrPlayer, selectedPlayerTeam, zoneClickString)
        averages.cur_shot = zoneClickString
        averages.cur_selection = teamOrPlayer
        # print(vars(averages).items())
        draw_circles(ax,
                     int(zoneClickString[0]),
                     shot_data,
                     averages,
                     teamOrPlayer)
        label = labels_8ft if zoneClickString == "8ft Range" else labels_5ft
        if teamOrPlayer == "Player":
            volume = averages.shot_player_avg_8ft_attempts\
                if zoneClickString == "8ft Range" \
                else averages.shot_player_avg_5ft_attempts
        else:
            volume = averages.shot_team_avg_8ft_attempts \
                if zoneClickString == "8ft Range" \
                else averages.shot_team_avg_5ft_attempts
        add_for_player = 3 if teamOrPlayer == "Player" else 0
        shots = [shot_data.iloc[0, 3 + add_for_player + 3 * spots]
                 for spots in range(4 if int(zoneClickString[0]) == 8 else 6)]
        player_team_avg = [shot_data.iloc[0, 4 + 3 * spots + add_for_player]
                           for spots in range(4 if
                           int(zoneClickString[0]) == 8 else 6)]
        shot_list = list(zip(label, shots, ['Specific Attempts' for spots in
                         range(4 if int(zoneClickString[0]) == 8 else 6)]))
        league_shots_list = list(
            zip(
                label, volume, [
                    'League Average Attempts' for spots in range(
                        4 if int(
                            zoneClickString[0]) == 8 else 6)]))
        player_team_shot_avg = list(zip(label, player_team_avg, [
                                    'Current Average' for spots in
                                    range(4 if int(zoneClickString[0])
                                        == 8 else 6)]))
        leauge_avg = list(zip(label, averages[0::], [
                          'League Average' for spots in range(4 if
                              int(zoneClickString[0]) == 8 else 6)]))
        shot_list.extend(league_shots_list)
        player_team_shot_avg.extend(leauge_avg)
        df = pd.DataFrame(
            shot_list,
            columns=[
                'Distance',
                'Volume',
                "Attempts"])
        df2 = pd.DataFrame(
            player_team_shot_avg, columns=[
                'Distance', 'Average', "Label"])
        ax2.clear()
        ax3.clear()
        sns.set_style("whitegrid")
        sns.set_style("dark")
        g = sns.barplot(
            ax=ax2,
            x='Distance',
            y='Volume',
            hue='Attempts',
            data=df,
            palette="deep")
        g.set_xticklabels(labels=g.get_xticklabels(), rotation=90)
        ax2.set_title("Attempts vs Average League Attempts")
        if(teamOrPlayer != 'Player'):
            ax2.set_ylim(0, averages.get_max_attempts())
        canvas2.draw()
        g2 = sns.barplot(
            ax=ax3,
            x='Distance',
            y='Average',
            hue='Label',
            data=df2,
            palette="deep")
        g2.set_xticklabels(labels=g.get_xticklabels(), rotation=90)
        ax3.set_title("Current Average vs League Average")
        canvas3.draw()

    canvas.draw()
    last_player_team = selectedPlayerTeam
    lastzone = zoneClickString
    last_PT_Type = teamOrPlayer

    after_queue.append(root.after(100, update))


if __name__ == "__main__":
    """
    Will run the main UI of the shot charts
    """

    root = tkinter.Tk()
    root.geometry("1400x800+300+100")

    frame1 = tkinter.Frame(root)

    averages = PlayerTeamAverage()
    fig2 = plt.figure(figsize=(4, 4))
    ax2 = fig2.add_subplot(111)
    ax2.set_title("Attempts vs Average League Attempts")
    canvas2 = FigureCanvasTkAgg(fig2, master=root)
    canvas2.get_tk_widget().grid(row=0, column=1)
    plt.tight_layout()
    plt.xlim(0, 6)
    plt.gcf().subplots_adjust(bottom=0.35, left=.2)
    ax2.set_ylim(0, averages.get_max_attempts())

    canvas2.draw()

    fig3 = plt.figure(figsize=(4, 4))
    ax3 = fig3.add_subplot(111)
    ax3.set_title("Current Average vs League Average")
    sns.barplot(ax=ax3, x=labels_5ft, y=[0, 0, 0, 0, 0, 0])
    plt.xticks(rotation=90)
    canvas3 = FigureCanvasTkAgg(fig3, master=root)
    canvas3.get_tk_widget().grid(row=1, column=1)
    plt.tight_layout()
    plt.gcf().subplots_adjust(bottom=0.35, left=.2)
    ax3.set_ylim(0, 1)
    canvas3.draw()

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111)
    draw_court(ax)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.xlim(-250, 250)
    plt.ylim(422.5, -47.5)

    canvas = FigureCanvasTkAgg(fig, master=frame1)  # A tk.DrawingArea.
    canvas.draw()

    frame1.grid(row=0, column=0, rowspan=2)

    ZoneOrDistance = Label(frame1, text="ZoneDistance", anchor='w')
    ZoneOrDistanceList = ["5ft Range", "8ft Range"]
    playerOrTeam = Label(frame1, text="Team/Player", anchor='w')
    playerOrTeamList = ["Team", "Player"]

    ZoneClikced = StringVar()
    ZoneClikced.set("5ft Range")
    ZoneDrop = OptionMenu(frame1, ZoneClikced, *ZoneOrDistanceList)
    ZoneOrDistance.grid(row=1, column=1)
    ZoneDrop.grid(row=2, column=1)

    playerOrTeamClicked = StringVar()
    playerOrTeamClicked.set("Team")
    playerTeamDrop = OptionMenu(frame1, playerOrTeamClicked, *playerOrTeamList)
    playerOrTeam.grid(row=1, column=2)
    playerTeamDrop.grid(row=2, column=2)
    listbox = Listbox(
        frame1,
        width=40,
        height=45,
        selectmode=SINGLE,
        exportselection=False)
    listbox.grid(row=3, column=2, rowspan=3)
    canvas.get_tk_widget().grid(row=3, column=1)
    root.title("NBA SHOT CHART")
    root.protocol("WM_DELETE_WINDOW", close_window)
    update()
    root.mainloop()
