import  tkinter
from  tkinter import  *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
from DrawCourt import draw_court
import matplotlib.pyplot as plt
from draw_ranges import *
from team_or_players import  *
from get_shots import  *


root = None
listbox = None
ftlist = []
lastzone = ""
last_PT_Type = ""
last_player_team = ""


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
	global lastzone
	global last_PT_Type
	global last_player_team

	selectedPlayerTeam = list_select()


	zoneClickString = ZoneClikced.get()
	teamOrPlayer = playerOrTeamClicked.get()

	if(last_PT_Type !=  teamOrPlayer):
		listbox.delete(0,END)
		listFill = get_all(teamOrPlayer)
		for item in listFill:
			listbox.insert(END, item)

	if(selectedPlayerTeam == ""):
		selectedPlayerTeam = last_player_team

	if(ZoneClikced.get() == lastzone 
		and (selectedPlayerTeam == last_player_team)):
		root.after(100, update)
		return

	remove_fts()
	draw_court()


	
	if(len(selectedPlayerTeam) != 0 and zoneClickString != "By Zone"):
		shot_data = get_shot(teamOrPlayer == "Player", selectedPlayerTeam)
		draw_circles(int(zoneClickString[0]), shot_data)

	canvas.draw()

	last_player_team = selectedPlayerTeam
	lastzone = zoneClickString
	last_PT_Type = teamOrPlayer

	root.after(100, update)



if __name__ == "__main__":
	"""
	Will run the main UI of the shot charts
	"""

	root = tkinter.Tk()
	root.geometry("1200x800+300+100")
	fig = plt.figure(figsize=(7,7))
	ax = draw_court()
	plt.xlim(-250,250)
	plt.ylim(422.5, -47.5)

	canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
	canvas.draw()

	button = tkinter.Button(master=root, text="Quit", command=root.quit)
	ZoneOrDistance = Label(root, text = "Zone/Distance", anchor='w')
	ZoneOrDistanceList = ["5ft Range", "8ft Range", "By Zone"]
	
	playerOrTeam = Label(root, text = "Team/Player", anchor='w')
	playerOrTeamList = ["Team", "Player"]

	ZoneClikced = StringVar()
	ZoneClikced.set("5ft Range")
	ZoneDrop = OptionMenu(root, ZoneClikced, *ZoneOrDistanceList)
	ZoneOrDistance.grid(row = 1, column = 1)
	ZoneDrop.grid(row = 2, column = 1)

	playerOrTeamClicked = StringVar()
	playerOrTeamClicked.set("Team")
	playerTeamDrop = OptionMenu(root, playerOrTeamClicked, *playerOrTeamList)
	playerOrTeam.grid(row = 1, column = 2)
	playerTeamDrop.grid(row = 2, column = 2)

	listbox = Listbox(root, width = 40, height = 30, selectmode = SINGLE, exportselection  = False)
	listbox.grid(row = 3, column = 2, rowspan=3)

	button.grid(row = 4, column = 1)
	canvas.get_tk_widget().grid(row = 3, column = 1)
	root.after(100, update)
	root.mainloop()

