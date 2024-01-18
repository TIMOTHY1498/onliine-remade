import webview
from tkinter import *
from tkinter import ttk

tk = Tk()
tk.geometry('1280x780')
webview.create_window('mainUI', 'file://F:/index.html') 
webview.start() 
tk.mainloop