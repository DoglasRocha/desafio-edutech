from tkinter import Tk, ttk
from tkinter import *
from insert_teacher_screen import InsertTeacherScreen
from insert_student_screen import InsertStudentScreen
from screen import Screen
from assets import button, label

class UserInterface(Screen):
    
    def __init__(self) -> None:
        self.window = Tk()
        self.mainframe = ttk.Frame(self.window, padding='5')
        self.__set_all_buttons()
        
        self.configure_screen('Escola Edutech')
        self.window.mainloop()
        
    def __set_all_buttons(self) -> None:
        button(self.mainframe, 'Inserir Professor', 2, 1, (W,E),
               self.__set_insert_teacher_screen)
        
        button(self.mainframe, 'Inserir aluno', 2, 2, (W,E),
               self.__set_insert_students_screen)
        
        button(self.mainframe, 'Visualizar Professores', 2, 3, (W,E),
               self.__set_teachers_table_screen)
        
        button(self.mainframe, 'Visualizar Alunos', 2, 4, (W,E),
               self.__set_students_table_screen)
        
        label(self.mainframe, 2, 5, (W,E))
        
        button(self.mainframe, 'Sair', 2, 6, (W,E), exit)
    
    def __set_insert_teacher_screen(self) -> None:
        InsertTeacherScreen(self.window)
            
    def __set_insert_students_screen(self) -> None:
        InsertStudentScreen(self.window)
        
    def __set_teachers_table_screen(self) -> None:
        pass

    def __set_students_table_screen(self) -> None:
        pass        
        
UserInterface()