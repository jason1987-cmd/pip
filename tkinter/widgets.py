# Tkinter in Py3

from tkinter import *

def ourGUIWindow():
    window=Tk()
    window.title("Login Window")
    window.geometry("600x400")
    Label(text="Login", bg="pink", width='600', height='2', font=('Calibri', 13)).pack()
    Label().pack()
    Label(text="Email").pack()
    Entry().pack()
    Label(text='Password').pack()
    Entry().pack()
    Label().pack()
    Button(text='Login', bg='green', height='1', fg='white', width='16').pack()
    window.mainloop()

ourGUIWindow()