from tkinter import ttk
from tkinter import *
from typing import Iterable

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
                 command: callable=lambda: None) -> None:
    
    _radio_button = ttk.Radiobutton(mainframe, variable=variable, 
                                    text=text, value=value,
                                    command=command)
    _radio_button.grid(column=column, row=row, sticky=sticky)
    return _radio_button
                    
def table_cell(mainframe: ttk.Frame, column: int, row: int, 
               sticky:tuple = (W,E), text: str='', color='white') -> None:
    
    _label =  Label(mainframe, text=text, bg=color, borderwidth=2, 
                 relief='ridge', padx=0, pady=0, width=30)
    _label.grid(column=column,row=row, sticky=sticky)
    return _label

def search_bar(frame: Frame, initial_column: int, row: int,
               text_variable: StringVar, label_text: str,
               command: callable=lambda: None) -> None:
    
    label(frame, initial_column, row, (W,E), label_text)
    entry(frame, text_variable, initial_column + 1, row)
    button(frame, 'Pesquisar', initial_column + 2, row, (W,E),
           command)
    
    for child in frame.winfo_children():
        child.grid_configure(padx=5)
        
def destroy_children(frame: Frame) -> None:
    
    for child in frame.winfo_children():
        child.destroy()
        
def create_table_titles(titles: Iterable, table_frame: Frame, 
                        row: int) -> None:
    
    column = 0
    
    for title in titles:
        table_cell(table_frame, column, row, (W,E), title, 'yellow')
        column += 1
        
def create_table(data: list, frame: Frame, row: int) -> None:
    
    for member in data:
        column = 0
        for information in member:
            table_cell(frame, column, row, text=information)
            column += 1
        row += 1