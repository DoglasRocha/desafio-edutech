from tkinter import *
from tkinter import ttk
from table_screen import TableScreen
from program_messenger import ProgramMessenger
from assets import table_cell

class StudentsTableScreen(TableScreen):
    
    def __init__(self, root: Tk) -> None:
        
        self.__window = Toplevel(root)
        self.__mainframe = ttk.Frame(self.__window, padding=0)
        self.__canvas = Canvas(self.__mainframe)
        # self.__scrollbar = Scrollbar(self.__mainframe, 
        #                             orient='vertical')
        self.__tableframe = Frame(self.__canvas)
        
        '''self.__one_cell_height = 0
        self.__one_cell_width = 0'''
        self.__rows = 1
        
        self.__set_column_titles()
        self.__set_data_cells()
        super().__init__(self.__window, self.__mainframe, self.__canvas,
                         self.__tableframe, 'Alunos')
            
    def __set_column_titles(self) -> None:
        
        table_cell(self.__tableframe, 0, 0, (W,E), 'Nome', 'yellow')
        table_cell(self.__tableframe, 1, 0, (W,E), 'Email', 'yellow')
        table_cell(self.__tableframe, 2, 0, (W,E), 'Turma', 'yellow')
        table_cell(self.__tableframe, 3, 0, (W,E), 'CGM', 'yellow')
        table_cell(self.__tableframe, 4, 0, (W,E), 'Turno', 'yellow')
        table_cell(self.__tableframe, 5, 0, (W,E), 'Status', 'yellow')
        cell = table_cell(self.__tableframe, 6, 0, (W,E), 'Professor', 'yellow')
        
        '''self.__one_cell_height = cell.winfo_reqheight()
        self.__one_cell_width = cell.winfo_reqwidth()'''
        
    def __set_data_cells(self) -> None:
        
        students = ProgramMessenger.select_all_students()
        
        for student in students:
            column = 0
            for data in student:
                table_cell(self.__tableframe, column, self.__rows, text=data)
                column += 1
            self.__rows += 1
            