from abc import ABCMeta
from tkinter import *

class InsertMemberScreen(metaclass=ABCMeta):
    
    def configure_screen(self) -> None:
        
        self.window.title('Inserir Aluno')
        self.mainframe.grid(column=0, row=0, sticky=(N,S,W,E))
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=10, pady=2.5)