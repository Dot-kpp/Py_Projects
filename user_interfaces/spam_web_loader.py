import tkinter
from tkinter import PhotoImage
from tkinter import Canvas
import customtkinter
import random
import webbrowser
import time



root_tk = tkinter.Tk()
root_tk.geometry("500x400")
root_tk.resizable(False, False)
root_tk.title("Settings_UI")

value = 1
luck = 0


bg = PhotoImage(file = "./background.png")
canvas1 = Canvas( root_tk, width = 500,
                 height = 400)

canvas1.pack(fill = "both", expand = True)

canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

def slider_event(value):
    value = int(value * 100 / 10)
    print(value)

def test1():
    print("lul")
    # time.sleep(3)
    # webbrowser.open('https://bit.ly/2PHfJn2')
    # time.sleep(3)
    # random.choice(test_button_list)()

test_button_list = [test1]

def button_function():
        print("Told you..")
        random.choice(test_button_list)()

def button_function_two():
    luck = random.choice(['win', 'lose', 'draw'])
    print(luck)

button = customtkinter.CTkButton(master=root_tk,
                                 fg_color=("green", "red"),
                                 text="Do not press",
                                 command=button_function,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=0)
button.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=root_tk,
                                 fg_color=("green", "red"),
                                 text="Test your luck",
                                 command=button_function_two,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=0)
button.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=root_tk,
                                 fg_color=("red", "grey"),
                                 text="Quit",
                                 command=root_tk.destroy,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=0)
button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

slider = customtkinter.CTkSlider(master=root_tk,
                                 bg_color=("grey"),
                                 width=190,
                                 height=16,
                                 border_width=0,
                                 command=slider_event)
slider.place(relx=0.65, rely=0.3, anchor=tkinter.CENTER)

root_tk.mainloop()