from tkinter import *
from tkinter import StringVar, Toplevel, messagebox, ttk
from screen import Screen
from program_messenger import ProgramMessenger
from assets import button, label, table_cell

class StudentsTableScreen(Screen):
    
    def __init__(self, root: Tk) -> None:
        
        self.__window = Toplevel(root)
        self.__mainframe = ttk.Frame(self.__window, padding=0)
        self.__canvas = Canvas(self.__mainframe)
        # self.__scrollbar = Scrollbar(self.__mainframe, 
        #                             orient='vertical')
        self.__tableframe = Frame(self.__canvas)
        
        self.__one_cell_height = 0
        self.__one_cell_width = 0
        self.__rows = 1
        
        self.__set_column_titles()
        self.__set_data_cells()
        self.__configure_mainframe()
        self.__configure_canvas()
        # self.__configure_scrollbar()
        
        self.configure_screen('Tabela de Professores', self.__window,
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
        self.__canvas.config(height=self.__one_cell_height * 7, 
                                width=self.__one_cell_width * 7)
                                # + self.__scrollbar.winfo_reqwidth()
                                # + 30)
        self.__canvas.create_window((0,0), window=self.__tableframe,
                                    anchor='nw')
        
    def __configure_tableframe(self) -> None:
        
        self.__tableframe.grid(column=0, row=0, sticky=(N,S,E,W))
        # self.__canvas.config(scrollregion=self.__canvas.bbox('all'))
        
    '''def __configure_scrollbar(self) -> None:
        
        self.__scrollbar.grid(column=2, row=0, sticky=(N,S))'''
            
    def __set_column_titles(self) -> None:
        
        table_cell(self.__tableframe, 0, 0, (W,E), 'Nome', 'yellow')
        table_cell(self.__tableframe, 1, 0, (W,E), 'Email', 'yellow')
        table_cell(self.__tableframe, 2, 0, (W,E), 'Turma', 'yellow')
        table_cell(self.__tableframe, 3, 0, (W,E), 'CGM', 'yellow')
        table_cell(self.__tableframe, 4, 0, (W,E), 'Turno', 'yellow')
        table_cell(self.__tableframe, 5, 0, (W,E), 'Status', 'yellow')
        cell = table_cell(self.__tableframe, 6, 0, (W,E), 'Professor', 'yellow')
        
        self.__one_cell_height = cell.winfo_reqheight()
        self.__one_cell_width = cell.winfo_reqwidth()
        
    def __set_data_cells(self) -> None:
        
        students = ProgramMessenger.select_all_students()
        
        for student in students:
            column = 0
            for data in student:
                table_cell(self.__tableframe, column, self.__rows, text=data)
                column += 1
            self.__rows += 1
            