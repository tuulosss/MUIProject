import tkinter as tk
from customtkinter import *



def change_color(color):
    global draw_color
    draw_color = color

def drawButtons(app):

    #colors = ["red","green","blue","black","yellow"]
    #for color in colors:
    #    button = CTKButton(app, text="", fg_color=color, command=lambda: change_color(color, width=30))

        
    button_red = CTkButton(app,text="", fg_color="red", command=lambda: change_color("red"),width=30)
    button_green = CTkButton(app,text="", fg_color="green", command=lambda: change_color("green"),width=30)
    button_blue = CTkButton(app,text="", fg_color="blue", command=lambda: change_color("blue"),width=30)
    button_black = CTkButton(app,text="", fg_color="black", command=lambda: change_color("black"),width=30)
    button_yellow = CTkButton(app,text="", fg_color="yellow", command=lambda: change_color("yellow"),width=30)

    button_green.place(x=0, y=120)
    button_blue.place(x=0, y=150)
    button_black.place(x=0, y=180)
    button_yellow.place(x=0, y=210)
    button_red.place(x=0, y=240)

    font_scale = CTkSlider(app, from_=1, to=10)
    font_scale.place(x=0, y=0)
    font_scale.set(1)
