
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
import numpy as np
import seaborn as sns 
import pandas as pd
import os

#Establishing connection to py_ball
HEADERS = {'Connection': 'keep-alive',
           'Host': 'stats.nba.com',
           'Origin': 'http://stats.nba.com',
           'Upgrade-Insecure-Requests': '1',
           'Referer': 'stats.nba.com',
           'x-nba-stats-origin': 'stats',
           'x-nba-stats-token': 'true',
           'Accept-Language': 'en-US,en;q=0.9',
           "X-NewRelic-ID": "VQECWF5UChAHUlNTBwgBVw==",
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)' +\
                         ' AppleWebKit/537.36 (KHTML, like Gecko)' + \
                         ' Chrome/81.0.4044.129 Safari/537.36'}

#Read in shot chart
shot_chart = pd.read_csv(r'/home/neil/Desktop/shotchart.csv')

class ShotCharts:
    def __init__(self,name,season):
        self.name = name
        self.season = season
        

        
    def create_court(ax: plt.axes, color="Black") -> plt.axes:
        """ Create a basketball court in a matplotlib axes
        """
        # Short corner 3PT lines
        ax.plot([-220.5,-220], [0, 140], linewidth=2, color=color)
        ax.plot([220, 220], [0, 140], linewidth=2, color=color)
        # 3PT Arc
        ax.add_artist(Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))
        # Lane and Key
        ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
        ax.plot([80, 80], [0, 190], linewidth=2, color=color)
        ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
        ax.plot([60, 60], [0, 190], linewidth=2, color=color)
        ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
        ax.add_artist(Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))
        ax.plot([-250, 250], [0, 0], linewidth=2, color='Black')
        # Rim
        ax.add_artist(Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))
        # Backboard
        ax.plot([-30, 30], [40, 40], linewidth=2, color=color)
        # Remove ticks
        ax.set_xticks([])
        ax.set_yticks([])
        # Set axis limits
        ax.set_xlim(-250, 250)
        ax.set_ylim(0, 470)
        return ax

        
    def volume_chart( name: str, season=None, 
                        RA=True,
                        extent=(-250, 250, 422.5, -47.5),
                        gridsize=25, cmap="Blues"):
        fig = plt.figure(figsize=(3.6, 3.6), facecolor='gainsboro', edgecolor='gainsboro', dpi=100)
        ax = fig.add_axes([0, 0, 1, 1], facecolor='gainsboro')

        player_df = shot_chart[shot_chart['PLAYER_NAME'] == name]

        # Plot hexbin of shots
    
        x = player_df.LOC_X
        y = player_df.LOC_Y + 60
        makes = player_df.SHOT_MADE_FLAG == 1 
        # Annotate player name and season
        #plt.text(-225, 430, f"{name}", fontsize=21, color='Black',
        #                        fontname='Corbel')
        plt.text(-225, 430, "Shot Selection Volume", fontsize=16, color='Black',
                                fontname='Corbel')
        season = f"{season[0][:4]}-{season[-1][-2:]}"
        plt.text(-250, -20, season, fontsize=8, color='Black')
        plt.text(110, -20, '@neilmaniar3', fontsize=8, color='Black')

        hexbin = ax.hexbin(x, y, cmap=cmap,
                        bins="log", gridsize=25, mincnt=2, extent=(-250, 250, 422.5, -47.5))
                
                       
        values = hexbin.get_array()
                
        mx = values.max()
        mn = values.min()
               

        # Draw court
        ax = ShotCharts.create_court(ax, 'black')

        # add legend
                
        cax = fig.add_axes([0.85, 0.65, 0.05, 0.3]) 
        cbar = fig.colorbar(hexbin,cax=cax)
               
        cbar.set_ticks([mn,mx])
        cbar.set_ticklabels(['Low','High'])
        cbar.ax.tick_params(rotation=90)

        

        
        plt.savefig('/home/neil/NBA_Analysis_Report/NBA_Analysis_Reports/resources/shotvolume_plot.png')

        
               
                
        return fig

