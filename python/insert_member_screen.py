from abc import ABCMeta
import tkinter

class InsertMemberScreen(metaclass=ABCMeta):
    
    def __configure_screen(self) -> None:
        
        self.__window.title('Inserir Aluno')
        self.__mainframe.grid(column=0, row=0, sticky=(N,S,W,E))
        self.__window.columnconfigure(0, weight=1)
        self.__window.rowconfigure(0, weight=1)
        
        for child in self.__mainframe.winfo_children():
            child.grid_configure(padx=10, pady=2.5)