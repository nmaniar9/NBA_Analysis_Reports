from fpdf import FPDF


import numpy as np

import pandas as pd
import PIL.Image
from PIL import ImageTk
from tkinter import *
import os
from shot_charts_create import ShotCharts
from get_playerstats import player_attr


name = 'Joel Embiid'
seasons = ['2022-23']
position = 'Center'
team = '76ers'
ShotCharts.volume_chart(name, seasons)
player_attr.get_headshot('203954')
player_attr.get_logo('1610612755')

hd = 'resources/headshot.png'
lg = 'resources/logo.png'
img = 'resources/shotvolume_plot.png'
title = 'Player Evaluation: ' + name
report_name = name +'_22_23season.pdf'



def create_report(title,position,team,report_name,img,hd,lg):
    pdf = FPDF(orientation = 'L', unit='mm', format='A4')
    pdf.set_margins(0,0,0)
    pdf.add_page()
    pdf.set_auto_page_break(False, margin = 0.0)

    header(pdf,title,position,team)
    volume_chart(pdf,img)
    headshot(pdf,hd)
    logo(pdf,lg)
    footer(pdf)
    export(pdf,report_name)

    pass

def header(pdf,title,position,team):
    
    pdf.set_font('Arial','B',15)
    pdf.set_fill_color(168, 66, 50)
        
    pdf.cell(400,20,txt=title,border=0,ln=0,align='',fill = True)
        
    pdf.set_y(10)
        #self.set_fill_color(19, 144, 161)
    pdf.set_font('Arial','',10)
    pdf.cell(400,10,txt=position + ' | ' + team,border=0,ln=0,align='',fill = False)

    return(pdf)

def headshot(pdf,hd):
    pdf.image(hd,150,0,30,20)

    return(pdf)

def logo(pdf,lg):
    pdf.image(lg,100,0,30,20)

    return(pdf)

def volume_chart(pdf,img):

    #pdf.add_page()
  
    pdf.image(img,180, 110,75,80)

    return(pdf)

    
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
        


create_report(title,position,team,report_name,img,hd,lg)
        








