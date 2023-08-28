
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

    def get_player_id(name):
        df = pd.read_csv(r'/home/neil/Desktop/file.csv')
        player_df =df[df['PLAYER_NAME'] == name]
        player_id = player_df.iloc[0]['PLAYER_ID']

        return(player_id)
    
    def get_team_id(name):
        df = pd.read_csv(r'/home/neil/Desktop/file.csv')
        player_df =df[df['PLAYER_NAME'] == name]
        team_id = player_df.iloc[0]['TEAM_ID']

        return(team_id)


    def off_rating(name):
        df = pd.read_csv(r'/home/neil/Desktop/file.csv')
        mean = df['OFF_RATING'].mean()

        player_df = df[df['PLAYER_NAME'] == name]
        player_mean = player_df['OFF_RATING'].mean()

        return(mean,player_mean)
    
    def def_rating(name):
        df = pd.read_csv(r'/home/neil/Desktop/file.csv')
        mean = df['DEF_RATING'].mean()

        player_df = df[df['PLAYER_NAME']==name]
        player_mean = player_df['DEF_RATING'].mean()

        return(mean,player_mean)

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




    def all_plots(stats_df):

        def format_year(year):
             return year[-2:]

        # Apply the formatting function to the 'year' column
        stats_df['year'] = stats_df['SEASON_ID'].apply(format_year)




 
        # Sample data
        x = stats_df['year']
        y1 = stats_df['GP']
        y2 = stats_df['PTS']
        y3 = stats_df['AST']
        y4 = stats_df['OREB']
        z4 = stats_df['DREB']

        # Create a 2x2 grid of subplots
        fig, axs = plt.subplots(2, 2, figsize=(10, 8))

        # Plot data on each subplot
        axs[0, 0].plot(x, y1, marker='o')
        axs[0, 0].set_title('Games Played')
        axs[0, 0].annotate(f'Max: {max(y1)}', xy=(0.5, 0.9), xycoords='axes fraction', fontsize=10, color='blue')
        axs[0, 0].annotate(f'Min: {min(y1)}', xy=(0.5, 0.8), xycoords='axes fraction', fontsize=10, color='blue')


        axs[0, 1].plot(x, y2, marker='o')
        axs[0, 1].set_title('Points')
        axs[0, 1].annotate(f'Max: {max(y2)}', xy=(0.5, 0.9), xycoords='axes fraction', fontsize=10, color='blue')
        axs[0, 1].annotate(f'Min: {min(y2)}', xy=(0.5, 0.8), xycoords='axes fraction', fontsize=10, color='blue')



        axs[1, 0].plot(x, y3, marker='o')
        axs[1, 0].set_title('Assists')
        axs[1, 0].annotate(f'Max: {max(y3)}', xy=(0.5, 0.9), xycoords='axes fraction', fontsize=10, color='blue')
        axs[1, 0].annotate(f'Min: {min(y3)}', xy=(0.5, 0.8), xycoords='axes fraction', fontsize=10, color='blue')




        line1, =axs[1, 1].plot(x, y4, marker='o')
        line2, =axs[1, 1].plot(x, z4, marker='s')
        axs[1, 1].annotate(f'Max: {max(y4)}', xy=(0.5, 0.9), xycoords='axes fraction', fontsize=10, color='orange')
        axs[1, 1].annotate(f'Min: {min(y4)}', xy=(0.5, 0.8), xycoords='axes fraction', fontsize=10, color='orange')
        axs[1, 1].annotate(f'Max: {max(y4)}', xy=(0.5, 0.4), xycoords='axes fraction', fontsize=10, color='blue')
        axs[1, 1].annotate(f'Min: {min(y4)}', xy=(0.5, 0.3), xycoords='axes fraction', fontsize=10, color='blue')

   







        axs[1, 1].set_title('Rebounds')

        axs[1, 1].legend([line1, line2], ['Offensive', 'Defensive'])

        # Adjust layout and spacing between subplots
        plt.tight_layout()

   
        plt.savefig('/home/neil/NBA_Analysis_Report/NBA_Analysis_Reports/resources/all_plots.png',transparent=True)
        plt.close()

    # Function to add annotations with arrows




    def get_stats(pid):
        stats = player.Player(headers=HEADERS,
                           endpoint='playercareerstats',
                           player_id=pid,
                           per_mode='Totals',
                           league_id='00'
                           )
        stats = pd.DataFrame(stats.data['SeasonTotalsRegularSeason'])

        return(stats)
    
    
