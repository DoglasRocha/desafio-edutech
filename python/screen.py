from abc import ABCMeta
from tkinter import *
from tkinter import ttk

class Screen(metaclass=ABCMeta):
    
    @staticmethod
    def configure_screen(title: str, window: Tk, mainframe: ttk.Frame) -> None:
        
        window.title(title)
        mainframe.grid(column=0, row=0, sticky=(N,S,W,E))
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)
        
        for child in mainframe.winfo_children():
            child.grid_configure(padx=10, pady=2.5)