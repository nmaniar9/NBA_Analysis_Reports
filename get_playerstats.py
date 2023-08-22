
import numpy as np
import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

from py_ball import player,image

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


class player_attr:
    

        
    def get_headshot(hd):
        headshot = image.Headshot(
               league='NBA',
               player_id=hd)
         
        headshot_im = headshot.image

        headshot_im.save("/home/neil/NBA_Analysis_Report/NBA_Analysis_Reports/resources/headshot.png")

 

    def get_logo(lg):
        logo = image.Logo (
                league='NBA',
                team_id=lg
          )
        
        logo.image.save('/home/neil/NBA_Analysis_Report/NBA_Analysis_Reports/resources/logo.png')


    def get_pid(name):
        pass

    def get_team(pid):
        pass

    def get_position(pid):
        pass

    def create_gamesplayed(stats_df):
        x = stats_df['SEASON_ID']
        y = stats_df['GP']
        plt.plot(x, y, marker='o')  # 'o' adds markers to data points
        #plt.title()
        #plt.xlabel('Season',fontsize=30)
        plt.ylabel('Games Played',fontsize=30)
        plt.grid(True)
        plt.annotate(f'Max Games Played: {max(y)}', xy=(x[y.idxmax()], max(y)), xytext=(20, -20),
             textcoords='offset points', arrowprops=dict(arrowstyle='->'))
        plt.annotate(f'Min Games Played: {min(y)}', xy=(x[y.idxmin()], min(y)), xytext=(20, 10),
             textcoords='offset points', arrowprops=dict(arrowstyle='->'))
        plt.savefig('/home/neil/NBA_Analysis_Report/NBA_Analysis_Reports/resources/games_played.png',transparent=True)
        plt.close()
        pass
    def create_pts(stats_df):
        x=stats_df['SEASON_ID']
        y=stats_df['PTS']
        plt.plot(x, y, marker='o')
        #plt.xlabel('Season',fontsize=27.5)
        plt.ylabel('Points',fontsize=25)
        plt.grid(True)
        plt.annotate(f'Max Points: {max(y)}', xy=(x[y.idxmax()], max(y)), xytext=(20, -20),
             textcoords='offset points', arrowprops=dict(arrowstyle='->'))
        plt.annotate(f'Min Points: {min(y)}', xy=(x[y.idxmin()], min(y)), xytext=(20, 10),
             textcoords='offset points', arrowprops=dict(arrowstyle='->'))
        plt.savefig('/home/neil/NBA_Analysis_Report/NBA_Analysis_Reports/resources/Points.png',transparent=True)
        plt.close()
    
    def create_reb(stats_df):
        x=stats_df['SEASON_ID']
        y=stats_df['OREB']
        z=stats_df['DREB']
        plt.plot(x, y, marker='o',label='Offensive')
        plt.plot(x, z, marker='s', label='Defensive')
        #plt.xlabel('Season',fontsize=30)
        plt.ylabel('Rebounds',fontsize=30)
        plt.legend()
        plt.grid(True)
        plt.annotate(f'Max Offensive Rebounds: {max(y)}', xy=(x[y.idxmax()], max(y)), xytext=(20, -20),
             textcoords='offset points', arrowprops=dict(arrowstyle='->'))
        plt.annotate(f'Min Offensive Rebounds: {min(y)}', xy=(x[y.idxmin()], min(y)), xytext=(20, 10),
             textcoords='offset points', arrowprops=dict(arrowstyle='->'))
        plt.annotate(f'Max Densive Rebounds: {max(z)}', xy=(x[z.idxmax()], max(z)), xytext=(20, -20),
             textcoords='offset points', arrowprops=dict(arrowstyle='->'))
        plt.annotate(f'Min Densive Rebounds: {min(z)}', xy=(x[z.idxmin()], min(z)), xytext=(20, 10),
             textcoords='offset points', arrowprops=dict(arrowstyle='->'))
        plt.savefig('/home/neil/NBA_Analysis_Report/NBA_Analysis_Reports/resources/rebounds.png',transparent=True)
        plt.close()

    def create_ast(stats_df):
        x=stats_df['SEASON_ID']
        y=stats_df['AST']
        plt.plot(x, y, marker='o')
        
        #plt.xlabel('Season',fontsize=30)
        plt.ylabel('Assist',fontsize=30)
        plt.grid(True)
        plt.annotate(f'Max Assits: {max(y)}', xy=(x[y.idxmax()], max(y)), xytext=(20, -20),
             textcoords='offset points', arrowprops=dict(arrowstyle='->'))
        plt.annotate(f'Min Assist: {min(y)}', xy=(x[y.idxmin()], min(y)), xytext=(20, 10),
             textcoords='offset points', arrowprops=dict(arrowstyle='->'))


        plt.savefig('/home/neil/NBA_Analysis_Report/NBA_Analysis_Reports/resources/assists.png',transparent=True)
        plt.close()









    def get_stats(pid):
        stats = player.Player(headers=HEADERS,
                           endpoint='playercareerstats',
                           player_id=pid,
                           per_mode='Totals',
                           league_id='00'
                           )
        stats = pd.DataFrame(stats.data['SeasonTotalsRegularSeason'])

        return(stats)
    
    
