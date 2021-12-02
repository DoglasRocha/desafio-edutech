from tkinter import StringVar, Toplevel, Tk, ttk, Frame, W, E 
from assets import (radio_button, search_bar, table_cell, label,
                    destroy_children)
from program_messenger import ProgramMessenger
from screen import Screen

class StudentsPerTeacher(Screen):
    
    def __init__(self, root: Tk) -> None:
        
        self.__window = Toplevel(root)
        self.__mainframe = ttk.Frame(self.__window)
        self.__searchbar_frame = Frame(self.__mainframe)
        self.__table_frame = Frame(self.__mainframe)
        self.__table = Frame(self.__mainframe)
        
        self.__searched_name = StringVar()
        self.__selected_teacher = StringVar()
        self.__row = 0
        
        self.__set_search_bar()
        self.configure_screen('Pesquisar Alunos do Professor', 
                              self.__window, self.__mainframe)
        
    def __set_search_bar(self) -> None:
        
        search_bar(self.__searchbar_frame, 0, self.__row, 
                   self.__searched_name, 'Nome:', self.__search_name)
        self.__row += 1
        
    def __search_name(self) -> None:
        
        names = ProgramMessenger.select_teacher(
            self.__searched_name.get())
        
        self.__set_search_result_and_selector(names)
        
    def __set_search_result_and_selector(self, result: list) -> None:
        
        destroy_children(self.__table_frame)
        destroy_children(self.__table)
            
        self.__row = 0
        self.__set_titles()
        
        for teacher in result:
            column = 0
            for data in teacher:
                table_cell(self.__table_frame, column, self.__row,
                           (W,E), data)
                if data == teacher[0]:
                    radio_button(self.__table_frame, 
                                 self.__selected_teacher,
                                 'Listar alunos deste professor',
                                 data, 5, self.__row, (W,E), 
                                 self.__set_table)
                column += 1
            
            self.__row += 1
            
        label(self.__table_frame, 0, self.__row)
        self.__row += 1
        
    def __set_titles(self) -> None:
        
        titles = ('Nome', 'Email', 'Turno')
        column = 0
        
        for title in titles:
            table_cell(self.__table_frame, column, self.__row, (W,E),
                       title, 'yellow')
            column += 1
        
        self.__row += 1
        
    def __set_table(self) -> None:
        
        result = ProgramMessenger.select_students_per_teacher(
            self.__selected_teacher.get()
        )
        
        self.__set_table_titles()
        
        column = 0
        for student in result:
            for data in student:
                table_cell(self.__table, column, self.__row, (W,E),
                           data)
                column += 1
            column = 0
            self.__row += 1
        
    def __set_table_titles(self) -> None:
        
        titles = ('Nome', 'Email', 'CGM', 'Turno', 'Turma', 'Professor')
        column = 0
        
        for title in titles:
            table_cell(self.__table, column, self.__row, (W,E),
                       title, 'yellow')
            column += 1
        
        self.__row += 1