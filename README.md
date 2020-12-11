# NBA_SHOT_CHART
NBA_SHOT_CHART produces a visualization of player or team 
shot charts. Selection of player or team can be done 
through the UI. As well as being able to choose the range
of shots of either 8ft or 5ft. There are a total of 3 plots for
visualization: Shot Chart on basketball court plot, 
Shot Attempts of Selected vs League Average Attempts, and 
Average of Selected vs Leauge Average. There are tkinter option
menus for selecting the distance ranges of the shots and whether a player or 
team will selected.
The data for the shot charts is produced by using the
nba_api library (https://github.com/swar/nba_api) and will
be parsed using pandas. The data will be held peristently through
pickle as not to time out the api. The visualization and UI will be 
made by using tkinter, matplotlib, and seaborn. 

### First-party modules:  
	tkinter  
	pickle  

### Third-part modules:  
	pandas  
	matplot_lib  
	nba_api  

## Installation
### Requirements:  
  pip install nba_api  
  pip install pandas  
  pip install matplotlib

## Code Strucutre
### UiMain.py  
 	Handles Displaying UI elements and tkinter windows. The values 
 	for the selected player/team and shot range is adjusted within this file.
 	The players and teams are listed within a listbox with the data visualized 
 	with matplotlib and seaborn plots to the left and right.  

### draw_court.py  
 	Credit to http://savvastjortjoglou.com/nba-shot-sharts.html for code for 
 	visualizing a basketball court in matplot lib that is functional with 
 	data provided by nba_api.  
### draw_ranges.py  
 	Creates the matplotlib elements (wedges) for displaying on the basketball court axes.  
### playerTeamClass.py  
 	Class for generating averages and shot attempts that remain constant throughout the
 	life time of the program. The magic methods are the __init__ for the initialization
 	of the class and __getitem__ to make the class subscriptable making the getting of the
 	averages within the drawing phase easier as there is no need to shuffle through
 	different arrays as the data will be preset with the class object.  
### team_or_players.py  
  Within the file the functions are for getting information of the nba players and teams.  
### get_shots.py  
  Contains function for getting the shot data of a single player or team.  


### Usage 
Select the desired ZoneDistance from the 
