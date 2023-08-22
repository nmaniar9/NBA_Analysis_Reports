
import numpy as np
import seaborn as sns 
import pandas as pd

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



    def get_stats(pid):
        

        stats = player.Player(headers=HEADERS,
                           endpoint='playercareerstats',
                           player_id=pid,
                           per_mode='Totals',
                           

                           league_id='00'
                           )
        stats = pd.DataFrame(stats.data['SeasonTotalsRegularSeason'])

        return(stats)
    
    
