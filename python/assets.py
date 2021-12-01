from tkinter import ttk
from tkinter import *

def button(mainframe: ttk.Frame, text: str, column: int, row: int,
           sticky: tuple, command: callable=lambda: None) -> None:
    
    _button = ttk.Button(mainframe, text=text, command=command)
    _button.grid(row=row, column=column, sticky=sticky)
    return _button
    
def label(mainframe: ttk.Frame, column: int, row: int,sticky: tuple=(),
          text: str='') -> None:
    
    _label = ttk.Label(mainframe, text=text)
    _label.grid(column=column, row=row, sticky=sticky)    
    return _label
    
def entry(mainframe: ttk.Frame, textvariable: StringVar, column: int,
          row: int) -> None:
    
    _entry = ttk.Entry(mainframe, textvariable=textvariable)
    _entry.grid(column=column,row=row, sticky=(W,E))
    return _entry
    
def radio_button(mainframe: ttk.Frame, variable: StringVar, text: str,
                 value: str, column: int, row: str, sticky: tuple=(),
                 command: callable= lambda: None) -> None:
    
    _radio_button = ttk.Radiobutton(mainframe, variable=variable, 
                                    text=text, value=value,
                                    command=command)
    _radio_button.grid(column=column, row=row, sticky=sticky)
    return _radio_button
                    
def table_cell(mainframe: ttk.Frame, column: int, row: int, 
               sticky:tuple = (), text: str='', color='white') -> None:
    
    _label =  Label(mainframe, text=text, bg=color, borderwidth=2, 
                 relief='ridge', padx=0, pady=0, width=30)
    _label.grid(column=column,row=row, sticky=(W,E))
    return _label