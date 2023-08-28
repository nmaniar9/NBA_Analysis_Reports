from fpdf import FPDF


import numpy as np

import pandas as pd
import PIL.Image
from PIL import ImageTk
from tkinter import *
import os
from shot_charts_create import ShotCharts
from get_playerstats import player_attr


name = 'Stephen Curry'
position = 'Point Gaurd'
team = 'Golden State Warriors'








def create_report(name,position,team):
    player_id = player_attr.get_player_id(name)
    team_id = player_attr.get_team_id(name)
    off_mean,off_player = player_attr.off_rating(name)
    def_mean,def_player = player_attr.def_rating(name)
    title = ' Player Evaluation: ' + name
    report_name = name +'_22_23season.pdf'
    seasons = ['2022-23']
    hd = 'resources/headshot.png'
    lg = 'resources/logo.png'
    img = 'resources/shotvolume_plot.png'
    ShotCharts.volume_chart(name, seasons)
    player_attr.get_headshot(player_id)
    player_attr.get_logo(team_id)
    stats_df = player_attr.get_stats(player_id)
    player_attr.all_plots(stats_df)



    pdf = FPDF(orientation = 'L', unit='mm', format='A4')
    pdf.set_margins(0,0,0)
    pdf.add_page()
    pdf.set_auto_page_break(False, margin = 0.0)

    header(pdf,title,position,team)
    volume_chart(pdf,stats_df)
    headshot(pdf,hd)
    logo(pdf,lg)
    season_charts(pdf)
    season_overview(pdf,stats_df)
    ratings(pdf,off_mean,off_player,def_mean,def_player)
    footer(pdf)
    export(pdf,report_name)
    

    pass

def header(pdf,title,position,team):

    pdf.set_y(10)
    pdf.set_x(35)

    pdf.set_font('Arial','B',20)
    

    pdf.cell(150,20,title,border=0,ln=0,align='',fill = False)
    pdf.set_y(10)
    pdf.set_x(170)
    pdf.set_font('Arial','B',15)
    pdf.cell(100,20,position + ' | ' + team)
    pdf.set_font('Arial','B',17)
    pdf.set_y(22)
    pdf.set_x(45)

    pdf.cell(237,20,'Regular Season: 2022-23',border=0,ln=0,align='',fill = False)
    

    return(pdf)


def headshot(pdf,hd):
    pdf.image(hd,2,5,43,35)

    return(pdf)

def logo(pdf,lg):
    pdf.image(lg,267,3,32,32)

    return(pdf)
def season_overview(pdf,stats_df):
    filter = stats_df[stats_df['SEASON_ID']=='2022-23']

    season = filter.iloc[0]['SEASON_ID']
    gp = filter.iloc[0]['GP']
    mpg = round(filter.iloc[0]['MIN']/gp,2)
    ppg = round(filter.iloc[0]['PTS']/gp,2)
    rpg = round(filter.iloc[0]['REB']/gp,2)
    ast = round(filter.iloc[0]['AST']/gp,2)
    stl = round(filter.iloc[0]['STL']/gp,2)
    blk = round(filter.iloc[0]['BLK']/gp,2)
    tov = round(filter.iloc[0]['TOV']/gp,2)

    
    pdf.set_y(40)
    pdf.set_x(19)
    pdf.set_font('Arial','B',15)
    pdf.cell(76.2,15,"Season Overview",align='',fill = False)

    pdf.image('resources/season_template.png',21,45,160,40)

    pdf.set_y(62)
    pdf.set_x(22)
    pdf.set_font('Arial','B',10)
    pdf.cell(65,10,str(season)+'        '+str(gp)+'            '+str(mpg)+'         '+str(ppg)+'          '+str(rpg)+'          '+str(ast)+'            '+str(stl)+'             '+str(blk)+'             '+str(tov),align='',fill = False)

def ratings(pdf,off_mean,off_player,def_mean,def_player):
    pdf.set_y(40)
    pdf.set_x(190)
    pdf.set_font('Arial','B',15)

    off_mean = round(off_mean,2)
    off_player = round(off_player,2)
    def_player = round(def_player,2)
    def_mean = round(def_mean,2)

    if(off_player > off_mean + 3):
        pdf.set_fill_color(109, 209, 94)
    elif(off_player < off_mean - 3):
        pdf.set_fill_color(252, 96, 96)
    else:
        pdf.set_fill_color(237, 227, 114)


    pdf.cell(65,10,'Offensive Rating',align='',fill = False)
    pdf.set_y(52)
    pdf.set_x(190)
    pdf.set_font('Arial','B',15)
    pdf.cell(45,21,str(off_player),align='C',border=1,fill = True)
    pdf.set_y(59)
    pdf.set_x(190)
    pdf.set_font('Arial','B',9)
    pdf.cell(45,23,'Average All Players: '+str(off_mean),align='',border=0,fill = False)


    if(def_player > def_mean + 3):
        pdf.set_fill_color(109, 209, 94)
    elif(def_player < def_mean - 3):
        pdf.set_fill_color(252, 96, 96)
    else:
        pdf.set_fill_color(237, 227, 114)    


    pdf.set_y(40)
    pdf.set_x(242)
    pdf.set_font('Arial','B',15)
    pdf.cell(65,10,'Defensive Rating',align='',fill = False)

    pdf.set_y(52)
    pdf.set_x(242)
    pdf.cell(45,21,str(def_player),align='C',border=1,fill = True)
    pdf.set_y(59)
    pdf.set_x(242)
    pdf.set_font('Arial','B',9)
    pdf.cell(45,23,'Average All Players: '+str(def_mean),align='',border=0,fill = False)






    

def volume_chart(pdf,stats_df):

    filter = stats_df[stats_df['SEASON_ID']=='2022-23']

    
    pdf.set_y(72)
    pdf.set_x(145)
    pdf.set_font('Arial','B',15)
    pdf.cell(76.2,15,"Shot Selection Volume",align='',fill = False) 
    pdf.image('resources/shotvolume_plot.png',145, 87.5,100,112)


    pdf.set_y(80.9)
    pdf.set_x(254)
    pdf.set_font('Arial','B',15)
    pdf.cell(76.2,15,"    FG%",align='',fill = False)
    pdf.image('resources/Hexagon.png',254,94.9,25.4,25.4)
   
    fg_pct = round(filter.iloc[0]['FG_PCT'] * 100,2)
    fg_at = filter.iloc[0]['FGA']
    fg_made = filter.iloc[0]['FGM']
    pdf.set_y(84.9)
    pdf.set_x(257)
    pdf.set_font('Arial','B',20)
    pdf.cell(76.2,40,str(fg_pct)+'%',align='',fill = False)
    pdf.set_y(91.9)
    pdf.set_x(260)
    pdf.set_font('Arial','B',10)
    pdf.cell(76.2,40,str(fg_made) + "/"+str(fg_at),align='',fill = False)


    pdf.set_y(118.9)
    pdf.set_x(254)
    pdf.set_font('Arial','B',15)
    pdf.cell(76.2,15," 3PT FG %",align='',fill = False)
    pdf.image('resources/Hexagon.png',254,130.9,25.4,25.4)

    fg_3pct = round(filter.iloc[0]['FG3_PCT'] * 100,2)
    fg_3at = filter.iloc[0]['FG3A']
    fg_3made = filter.iloc[0]['FG3M']
    pdf.set_y(121.9)
    pdf.set_x(257)
    pdf.set_font('Arial','B',20)
    pdf.cell(76.2,40,str(fg_3pct)+'%',align='',fill = False)
    pdf.set_y(128.9)
    pdf.set_x(260)
    pdf.set_font('Arial','B',10)
    pdf.cell(76.2,40,str(fg_3made) + "/"+str(fg_3at),align='',fill = False)


    pdf.set_y(154.9)
    pdf.set_x(254)
    pdf.set_font('Arial','B',15)
    pdf.cell(76.2,15,"     FT %",align='',fill = False)
    pdf.image('resources/Hexagon.png',254,166.9,25.4,25.4)
    ft_pct = round(filter.iloc[0]['FT_PCT'] * 100,2)
    ft_at = filter.iloc[0]['FTA']
    ft_made = filter.iloc[0]['FTM']
    pdf.set_y(157.9)
    pdf.set_x(257)
    pdf.set_font('Arial','B',20)
    pdf.cell(76.2,40,str(ft_pct)+'%',align='',fill = False)
    pdf.set_y(164.9)
    pdf.set_x(260)
    pdf.set_font('Arial','B',10)
    pdf.cell(76.2,40,str(ft_made) + "/"+str(ft_at),align='',fill = False)


    return(pdf)

def season_charts(pdf):

    pdf.image('resources/all_plots.png',19,82.5,120,120)


    pdf.set_y(72)
    pdf.set_x(19)
    pdf.set_font('Arial','B',15)
    pdf.cell(76.5,15,"Season Trends",align='',fill = False) 

    


    
def footer(pdf):
    #Position at 1.5cm from the bottom
    pdf.set_y(-10)
    #font
    pdf.set_font('Arial','B',10)
    pdf.set_fill_color(255, 255, 255)
    #title
    pdf.cell(0,6,'@nmaniar3',0,1,'L',1)
    pdf.ln(4)

    return(pdf)

        
def export(pdf,filename):

    pdf.output(filename,'F')

    pass
        


create_report(name,position,team)
        








