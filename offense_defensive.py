import numpy as np
import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

from py_ball import team

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

#Offensive formula
    #ORtg = 100 * (PProd / TotPoss)

'''
    ScPoss = (FG_Part + AST_Part + FT_Part) * (1 - (Team_ORB / Team_Scoring_Poss) 
                                           * Team_ORB_Weight * Team_Play%) + ORB_Part

    FG_Part = FGM * (1 - 0.5 * ((PTS - FTM) / (2 * FGA)) * qAST)
    qAST = ((MP / (Team_MP / 5)) * (1.14 * ((Team_AST - AST) / Team_FGM))) + ((((Team_AST / Team_MP) * MP * 5 - AST) / ((Team_FGM / Team_MP) * MP * 5 - FGM)) * (1 - (MP / (Team_MP / 5))))
    AST_Part = 0.5 * (((Team_PTS - Team_FTM) - (PTS - FTM)) / (2 * (Team_FGA - FGA))) * AST
    FT_Part = (1-(1-(FTM/FTA))^2)*0.4*FTA
    Team_Scoring_Poss = Team_FGM + (1 - (1 - (Team_FTM / Team_FTA))^2) * Team_FTA * 0.4
    Team_ORB_Weight = ((1 - Team_ORB%) * Team_Play%) / ((1 - Team_ORB%) * Team_Play% + Team_ORB% * (1 - Team_Play%))
    Team_ORB% = Team_ORB / (Team_ORB + (Opponent_TRB - Opponent_ORB))
    Team_Play% = Team_Scoring_Poss / (Team_FGA + Team_FTA * 0.4 + Team_TOV)
    ORB_Part = ORB * Team_ORB_Weight * Team_Play%

    FGxPoss = (FGA - FGM) * (1 - 1.07 * Team_ORB%)
    FTxPoss = ((1 - (FTM / FTA))^2) * 0.4 * FTA

    TotPoss = ScPoss + FGxPoss + FTxPoss + TOV

'''

class offensive_rating:
    def scposs(stats_df):
        team_stats = team.Team(headers=HEADERS,
                           endpoint='teamgamelogs',
                           team_id = '1610612755',
                           season = '2022-23',
                           
                           measure_type = 'Base',
                           
                           league_id='00')

        team_stats = pd.DataFrame(team_stats.data['TeamGameLogs'])

        team_minutes_df = team_stats['MIN'].astype('int')
        team_assist_df = team_stats['AST'].astype('int')
        team_offensive_rebounds_df = team_stats['OREB'].astype('int')
        team_defensive_rebounds_df = team_stats['DREB'].astype('int')
        team_fga_df = team_stats['FGA'].astype('int')
        team_fgm_df = team_stats['FGM'].astype('int')
        team_points_df = team_stats['PTS'].astype('int')


        filter = stats_df[stats_df['SEASON_ID']=='2022-23']

        fgm = filter.iloc[0]['FGM']
        fga = filter.iloc[0]['FGA']
        mp = filter.iloc[0]['MIN']
        
        
    