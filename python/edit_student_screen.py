from tkinter import StringVar, Toplevel, Tk, ttk, N,E,W,S
from screen import Screen
from assets import label, entry, button, radio_button, table_cell
from program_messenger import ProgramMessenger

class EditStudentScreen(Screen):
    
    def __init__(self, root: Tk) -> None:
        
        self.__window = Toplevel(root)
        self.__mainframe = ttk.Frame(self.__window)
        self.__searched_name = StringVar()
        self.__selected_student = StringVar()
        
        self.__name = StringVar()
        self.__email = StringVar()
        self.__class = StringVar()
        self.__CGM = StringVar()
        self.__shift = StringVar()
        self.__status = StringVar()
        self.__teacher = StringVar()
        self.__data = (self.__name, self.__email, self.__class,
                       self.__CGM, self.__shift, self.__status,
                       self.__teacher)
        
        self.__row = 0
        
        self.__set_search_bar()
        # self.__set_form()
        self.__set_buttons()
        self.configure_screen('Editar Estudante', self.__window,
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
        
    def __set_titles(self) -> None:
        
        titles = ('Nome', 'Email', 'CGM', 'Turma')
        column = 0
        for title in titles:
            table_cell(self.__mainframe, column, self.__row, (W,E), title, 'yellow')
            column += 1
            
        self.__row += 1
    
    def __set_form(self) -> None:
        
        self.__set_labels()
        student = ProgramMessenger.select_student(self.__selected_student
                                                  .get())[0]
        
        for i in range(len(self.__data)):
            self.__data[i].set(student[i])
            
        
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
        pass
        