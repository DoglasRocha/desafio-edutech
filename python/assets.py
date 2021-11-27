from tkinter import ttk
from tkinter import *

def button(mainframe: ttk.Frame, text: str, column: int, row: int,
           sticky: tuple, command: callable=lambda: None) -> None:
    ttk.Button(mainframe, text=text, command=command).grid(
        row=row, column=column, sticky=sticky)
    
def label(mainframe: ttk.Frame, column: int, row: int,
          sticky: tuple=(), text: str='') -> None:
    ttk.Label(mainframe, text=text).grid(
        column=column, row=row, sticky=sticky)
    
def entry(mainframe: ttk.Frame, textvariable: StringVar, column: int,
          row: int) -> None:
    ttk.Entry(mainframe, textvariable=textvariable).grid(
        column=column,row=row)
    
def radio_button(mainframe: ttk.Frame, variable: StringVar, text: str,
                 value: str, column: int, row: str, 
                 sticky: tuple=()) -> None:
    ttk.Radiobutton(mainframe, variable=variable, text=text, 
                    value=value).grid(
                        column=column, row=row, sticky=sticky)