from tkinter import StringVar, Toplevel, Tk, ttk, N,E,W,S
from screen import Screen
from assets import label, entry, button, radio_button, table_cell
from program_messenger import ProgramMessenger
from student_validator import StudentValidator

class EditStudentScreen(Screen, StudentValidator):
    
    def __init__(self, root: Tk) -> None:
        
        self._window = Toplevel(root)
        self.__mainframe = ttk.Frame(self._window)
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
        
        label(self.__mainframe, 0, self.__row, (W,E), 'Nome: ')
        entry(self.__mainframe, self.__searched_name, 1, self.__row)
        button(self.__mainframe, 'Pesquisar', 2, self.__row, (W,E), 
               self.__search_name)
        self.__row += 1
    
    def __search_name(self) -> None:
        names = ProgramMessenger.select_students_by_name(
            self.__searched_name.get())
        
        self.__set_search_result_and_selector(names)
    
    def __set_search_result_and_selector(self, result: list) -> None:
        
        self.__set_titles()
        
        for student in result:
            column = 0
            for data in student:
                table_cell(self.__mainframe, column, self.__row,
                           (W,E), data)
                if data == student[0]:
                    radio_button(self.__mainframe, 
                                 self.__selected_student,
                                 '', 
                                 data, 
                                 5, 
                                 self.__row,
                                 (W,E),
                                 self.__set_form)
                column += 1
            self.__row += 1
            self.__results += 1
            
        label(self.__mainframe, 0, self.__row)
        self.__row += 1
        
    def __set_titles(self) -> None:
        
        titles = ('Nome', 'Email', 'CGM', 'Turma')
        column = 0
        for title in titles:
            table_cell(self.__mainframe, column, self.__row, (W,E), title, 'yellow')
            column += 1
            
        self.__row += 1
    
    def __set_form(self) -> None:
        
        student = ProgramMessenger.select_student(self.__selected_student
                                                  .get())[0]
        
        for i in range(len(self._data)):
            self._data[i].set(student[i])
        
        if self.__row - self.__results < 6:     
            self.__set_labels()
            self.__set_entries()
            label(self.__mainframe, 0, self.__row)
            self.__row += 1
            self.__set_buttons()
            
    def __set_entries(self) -> None:
        
        label(self.__mainframe, 1, self.__row, (W,E), 
              text=self._name.get())
        entry(self.__mainframe, self._email, 3, self.__row)
        entry(self.__mainframe, self._class, 5, self.__row)
        self.__row += 1
        
        entry(self.__mainframe, self._CGM, 1, self.__row)
        radio_button(self.__mainframe, self._shift, 'Manhã', 'M',
                     3, self.__row, (W))
        radio_button(self.__mainframe, self._shift, 'Tarde', 'T',
                     4, self.__row, (W))
        self.__row += 1
        
        entry(self.__mainframe, self._teacher, 1, self.__row)     
        radio_button(self.__mainframe, self._status, 'Ativo', 'ATIVO',
                     3, self.__row, (W))
        radio_button(self.__mainframe, self._status, 'Inativo', 'INATIVO',
                     4, self.__row, (W))
        self.__row += 1  
        
    def __set_labels(self) -> None:
        
        label(self.__mainframe, 0, self.__row, text='Nome:')
        label(self.__mainframe, 2, self.__row, text='E-mail:')
        label(self.__mainframe, 4, self.__row, text='Turma:')
        self.__row += 1
        
        label(self.__mainframe, 0, self.__row, text='CGM:')
        label(self.__mainframe, 2, self.__row, text='Turno:')
        self.__row += 1
        
        label(self.__mainframe, 0, self.__row, text='Professor:')
        label(self.__mainframe, 2, self.__row, text='Status:')
        
        self.__row -= 2
    
    def __set_buttons(self) -> None:
        
        button(self.__mainframe, 'Cancelar', 5, self.__row, (W,E), 
               (self._window.destroy))
        
        pad = button(self.__mainframe, 'Editar Aluno', 6, self.__row, 
                     (W,E), self.try_to_create_student)
        
        pad.grid_configure(padx=10)
        