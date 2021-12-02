from tkinter import (StringVar, Toplevel, Tk, messagebox, ttk, N, E,
                     W, S, Frame)
from screen import Screen
from assets import label, entry, button, radio_button, search_bar, table_cell
from program_messenger import ProgramMessenger
from student_validator import StudentValidator

class EditStudentScreen(Screen, StudentValidator):
    
    def __init__(self, root: Tk) -> None:
        
        self._window = Toplevel(root)
        self.__mainframe = ttk.Frame(self._window)
        self.__seachbar_frame = Frame(self.__mainframe)
        self.__table_and_form_frame = Frame(self.__mainframe)
        self.__searched_name = StringVar()
        self.__selected_student = StringVar()
        
        self._name = StringVar()
        self._email = StringVar()
        self._class = StringVar()
        self._CGM = StringVar()
        self._shift = StringVar()
        self._status = StringVar()
        self._teacher = StringVar()
        self._data = (self._name, self._email, self._class,
                       self._CGM, self._shift, self._status,
                       self._teacher)
        
        self.__row = 0
        self.__results = 0
        
        self.__set_search_bar()
        self.configure_screen('Pesquisar Estudante', self._window,
                              self.__mainframe)
        
    def __set_search_bar(self) -> None:
        
        search_bar(self.__seachbar_frame, 0, self.__row, 
                   self.__searched_name, 'Nome:', self.__search_name)        
        self.__row += 1
    
    def __search_name(self) -> None:
        names = ProgramMessenger.select_students_by_name(
            self.__searched_name.get())
        print(names, self.__searched_name.get())
        
        self.__set_search_result_and_selector(names)
    
    def __set_search_result_and_selector(self, result: list) -> None:
        
        for child in self.__table_and_form_frame.winfo_children():
            child.destroy()
            
        self.__row = 0
        self.__set_titles()
            
        for student in result:
            column = 0
            for data in student:
                table_cell(self.__table_and_form_frame, column,
                           self.__row, (W,E), data)
                if data == student[0]:
                    radio_button(self.__table_and_form_frame, 
                                self.__selected_student,
                                'Editar este aluno', data, 5, 
                                self.__row, (W,E), self.__set_form)
                column += 1
                    
            self.__row += 1
            self.__results += 1
                
        label(self.__table_and_form_frame, 0, self.__row)
        self.__row += 1
        
    def __set_titles(self) -> None:
        
        titles = ('Nome', 'Email', 'CGM', 'Turma')
        column = 0
        
        for title in titles:
            table_cell(self.__table_and_form_frame, column, 
                       self.__row, (W,E), title, 'yellow')
            column += 1
            
        self.__row += 1
    
    def __set_form(self) -> None:
        
        student = ProgramMessenger.select_student(
            self.__selected_student.get())[0]
        
        for i in range(len(self._data)):
            self._data[i].set(student[i])
        
        if self.__row - self.__results < 6:     
            self.__set_labels()
            self.__set_entries()
            label(self.__table_and_form_frame, 0, self.__row)
            self.__row += 1
            self.__set_buttons()
            
    def __set_entries(self) -> None:
        
        label(self.__table_and_form_frame, 1, self.__row, (W,E), 
              text=self._name.get())
        entry(self.__table_and_form_frame, self._email, 3, self.__row)
        entry(self.__table_and_form_frame, self._class, 5, self.__row)
        self.__row += 1
        
        entry(self.__table_and_form_frame, self._CGM, 1, self.__row)
        radio_button(self.__table_and_form_frame, self._shift, 'Manhã',
                     'M', 3, self.__row, (W))
        radio_button(self.__table_and_form_frame, self._shift, 'Tarde', 
                     'T', 4, self.__row, (W))
        self.__row += 1
        
        entry(self.__table_and_form_frame, self._teacher, 1, self.__row)     
        radio_button(self.__table_and_form_frame, self._status, 'Ativo', 
                     'ATIVO', 3, self.__row, (W))
        radio_button(self.__table_and_form_frame, self._status, 'Inativo', 
                     'INATIVO', 4, self.__row, (W))
        self.__row += 1  
        
    def __set_labels(self) -> None:
        
        label(self.__table_and_form_frame, 0, self.__row, text='Nome:')
        label(self.__table_and_form_frame, 2, self.__row, text='E-mail:')
        label(self.__table_and_form_frame, 4, self.__row, text='Turma:')
        self.__row += 1
        
        label(self.__table_and_form_frame, 0, self.__row, text='CGM:')
        label(self.__table_and_form_frame, 2, self.__row, text='Turno:')
        self.__row += 1
        
        label(self.__table_and_form_frame, 0, self.__row, text='Professor:')
        label(self.__table_and_form_frame, 2, self.__row, text='Status:')
        
        self.__row -= 2
    
    def __set_buttons(self) -> None:
        
        button(self.__table_and_form_frame, 'Cancelar', 5, self.__row,
               (W,E), (self._window.destroy))
        
        pad = button(self.__table_and_form_frame, 'Editar Aluno', 6, 
                     self.__row, (W,E), self.try_to_create_student)
        
        pad.grid_configure(padx=10)
        