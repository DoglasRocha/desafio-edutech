from tkinter import *
from tkinter import StringVar, Toplevel, messagebox, ttk
from screen import Screen
from program_messenger import ProgramMessenger
from assets import button, label

class StudentsTableScreen(Screen):
    
    def __init__(self, root: Tk) -> None:
        
        self.__window = Toplevel(root)
        self.__mainframe = ttk.Frame(self.__window, padding='5')
        
        Screen.configure_screen('Tabela de Professores', self.__window,
                                self.__mainframe)