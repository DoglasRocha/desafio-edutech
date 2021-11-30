from tkinter import *
from tkinter import ttk
from table_screen import TableScreen
from program_messenger import ProgramMessenger
from assets import table_cell

class TeachersTableScreen(TableScreen):
    
    def __init__(self, root: Tk) -> None:
        
        self.__window = Toplevel(root)
        self.__mainframe = ttk.Frame(self.__window, padding=0)
        self.__canvas = Canvas(self.__mainframe)
        self.__tableframe = Frame(self.__canvas)
        
        self.__rows = 1
        
        self.__set_column_titles()
        self.__set_data_cells()
        super().__init__(self.__window, self.__mainframe, self.__canvas,
                         self.__tableframe, 'Professores')
    
    def __set_column_titles(self) -> None:
        
        table_cell(self.__tableframe, 0, 0, (W,E), 'Nome', 'yellow')
        table_cell(self.__tableframe, 1, 0, (W,E), 'Email', 'yellow')
        table_cell(self.__tableframe, 2, 0, (W,E), 'Turmas', 'yellow')
        table_cell(self.__tableframe, 3, 0, (W,E), 'Turno', 'yellow')
        
        '''self.__one_cell_height = cell.winfo_reqheight()
        self.__one_cell_width = cell.winfo_reqwidth()'''
        
    def __set_data_cells(self) -> None:
        
        teachers = ProgramMessenger.select_all_teachers()
        
        for teacher in teachers:
            column = 0
            for data in teacher:
                table_cell(self.__tableframe, column, self.__rows, text=data)
                column += 1
            self.__rows += 1
    