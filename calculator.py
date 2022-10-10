#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2022 mdfk <mdfk@Elite>

import tkinter as tk
from math import sqrt, factorial, pi

count = ""

####### functions #######
def clic(key):
    global count
    count = count + key
    calculation.set(count)

def delete_char():
    global count
    count = count[:-1]
    if count:
        calculation.set(count)
    else:
        calculation.set("0")

def clean_scr():
    global count
    count = ""
    calculation.set("0")


def calculate():
    global count
    try:
        total = str(eval(count))
    except Exception:
        clean_scr()
        total = "ERROR"
    calculation.set(total)


####### window #######

# Main windows
window = tk.Tk()
window.title("Calculator ACME")
window.config(width=440, height=600, bg="Light Steel Blue")
window.resizable(0,0)

# Variable in screen (result)
calculation = tk.StringVar()

clean_scr()

# Screen parameters
screen = tk.Entry(
                font=["arial",20,"bold"],
                width=24,         # width
                bd=20,            # grosor del borde
                bg="powder blue",  # color de fondo
                justify="right",      # alineación del texto
                state=tk.DISABLED,    # la hago solo lectura
                textvariable=calculation  # variable a mostrar
            )
screen.place(x=16, y=60)

# Buttons dimensions
width = 9
height = 2

#################   KEYS   #################
# key to delete
etiqueta = tk.Label(text="Practicas - EducacionIT",font=["Iovseka Nerd Font",12,"bold"],bg="Light Steel Blue",)
etiqueta.place(x=115,y=15)
button = tk.Button(text="\u2190", width=width, height=height, bg="SkyBlue", command=delete_char)
button.place(x=324, y=150)


## First row 1 2 3 +
button = tk.Button(text="1", width=width, height=height, command=lambda:clic("1"))
button.place(x=18, y=210)
button = tk.Button(text="2", width=width, height=height, command=lambda:clic("2"))
button.place(x=120, y=210)
button = tk.Button(text="3", width=width, height=height, command=lambda:clic("3"))
button.place(x=222, y=210)
button = tk.Button(text="+", width=width, height=height, bg="SteelBlue", command=lambda:clic("+"))
button.place(x=324, y=210)

## Second row 4 5 6 -
button = tk.Button(text="4", width=width, height=height, command=lambda:clic("4"))
button.place(x=18, y=270)
button = tk.Button(text="5", width=width, height=height, command=lambda:clic("5"))
button.place(x=120, y=270)
button = tk.Button(text="6", width=width, height=height, command=lambda:clic("6"))
button.place(x=222, y=270)
button = tk.Button(text="-", width=width, height=height, bg="SteelBlue", command=lambda:clic("-"))
button.place(x=324, y=270)

## Third row 7 8 9 x
button = tk.Button(text="7", width=width, height=height, command=lambda:clic("7"))
button.place(x=18, y=330)
button = tk.Button(text="8", width=width, height=height, command=lambda:clic("8"))
button.place(x=120, y=330)
button = tk.Button(text="9", width=width, height=height, command=lambda:clic("9"))
button.place(x=222, y=330)
button = tk.Button(text="x", width=width, height=height, bg="SteelBlue", command=lambda:clic("*"))
button.place(x=324, y=330)

## Fourth row ( 0 ) /
button = tk.Button(text="(", width=width, height=height, bg="SkyBlue", command=lambda:clic("("))
button.place(x=18, y=390)
button = tk.Button(text="0", width=width, height=height, command=lambda:clic("0"))
button.place(x=120, y=390)
button = tk.Button(text=")", width=width, height=height, bg="SkyBlue", command=lambda:clic(")"))
button.place(x=222, y=390)
button = tk.Button(text="/", width=width, height=height, bg="SteelBlue", command=lambda:clic("/"))
button.place(x=324, y=390)

## fifth row root comma power module
button = tk.Button(text="\u221A", width=width, height=height, bg="SkyBlue", command=lambda:clic("sqrt("))
button.place(x=18, y=450)
button = tk.Button(text=".", width=width, height=height, bg="SkyBlue", command=lambda:clic("."))
button.place(x=120, y=450)
button = tk.Button(text="POW", width=width, height=height, bg="SkyBlue", command=lambda:clic("**"))
button.place(x=222, y=450)
button = tk.Button(text="%", width=width, height=height, bg="SkyBlue", command=lambda:clic("%"))
button.place(x=324, y=450)

## Sixth row Clear factorial pi =
button = tk.Button(text="CL", width=width, height=height, bg="SkyBlue", command=clean_scr)
button.place(x=18, y=510)
button = tk.Button(text="!", width=width, height=height, bg="SkyBlue", command=lambda:clic("factorial("))
button.place(x=120, y=510)
button = tk.Button(text="\u03c0", width=width, height=height, bg="SkyBlue", command=lambda:clic(str(pi)))
button.place(x=222, y=510)
button = tk.Button(text="=", width=width, height=height, bg="medium aquamarine", command=calculate)
button.place(x=324, y=510)

window.mainloop()

