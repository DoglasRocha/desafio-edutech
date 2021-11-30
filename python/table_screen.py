from abc import ABCMeta
from screen import Screen
from tkinter import Toplevel, ttk, Canvas, Frame
from tkinter import N,S,E,W

class TableScreen(Screen):
    
    def __init__(self, window: Toplevel, mainframe: ttk.Frame,
                 canvas: Canvas, tableframe: Frame,
                 member: str) -> None:
        
        self.__window = window
        self.__mainframe = mainframe
        self.__canvas = canvas
        self.__tableframe = tableframe
        
        self.__configure_mainframe()
        self.__configure_canvas()
        # self.__configure_scrollbar()
        
        self.configure_screen(f'Tabela de {member}', self.__window,
                                self.__mainframe)
        self.__configure_tableframe()
        
    def __configure_mainframe(self) -> None:
        
        # self.__mainframe.grid_propagate(False)
        self.__mainframe.grid_columnconfigure(0, weight=1)
        self.__mainframe.grid_rowconfigure(0, weight=1)
        '''self.__mainframe.config(height=self.__one_cell_height * 7, 
                                width=self.__one_cell_width * 7)''' 
                                # + self.__scrollbar.winfo_reqwidth()
                                # + 30)
    
    def __configure_canvas(self) -> None:
        # self.__canvas.configure(yscrollcommand=self.__scrollbar.set)
        # self.__scrollbar.config(command=self.__canvas.yview)
        self.__canvas.grid(column=0, row=0, sticky='news')
        '''self.__canvas.config(height=self.__one_cell_height * 7, 
                                width=self.__one_cell_width * 7)'''
                                # + self.__scrollbar.winfo_reqwidth()
                                # + 30)
        self.__canvas.create_window((0,0), window=self.__tableframe,
                                    anchor='nw')
        
    def __configure_tableframe(self) -> None:
        
        self.__tableframe.grid(column=0, row=0, sticky=(N,S,E,W))
        # self.__canvas.config(scrollregion=self.__canvas.bbox('all'))
        
    '''def __configure_scrollbar(self) -> None:
        
        self.__scrollbar.grid(column=2, row=0, sticky=(N,S))'''