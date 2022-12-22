import tkinter
import customtkinter

root_tk = tkinter.Tk()
root_tk.geometry("300x250")
root_tk.title("Secret Yo Generator")

def button_function():
    print("Yoyoyoyoyo")

button = customtkinter.CTkButton(master=root_tk,
                                 fg_color=("black", "red"),  # <- tuple color for light and dark theme
                                 text="Do not press",
                                 command=button_function,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8)
button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

def slider_event(value):
    print("yo")

slider = customtkinter.CTkSlider(master=root_tk,
                                 width=160,
                                 height=16,
                                 border_width=5.5,
                                 command=slider_event)
slider.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

root_tk.mainloop()