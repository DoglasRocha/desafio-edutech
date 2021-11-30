from tkinter import Tk, ttk
from tkinter import *
from insert_teacher_screen import InsertTeacherScreen
from insert_student_screen import InsertStudentScreen
from students_table_screen import StudentsTableScreen
from teachers_table_screen import TeachersTableScreen
from screen import Screen
from assets import button, label

class UserInterface(Screen):
    
    def __init__(self) -> None:
        self.__root = Tk()
        self.__mainframe = ttk.Frame(self.__root, padding='5')
        self.__set_all_buttons()
        self.configure_screen('Escola Edutech', self.__root, 
                              self.__mainframe)
        self.__root.mainloop()
        
    def __set_all_buttons(self) -> None:
        button(self.__mainframe, 'Inserir Professor', 2, 1, (W,E),
               self.__set_insert_teacher_screen) 
        button(self.__mainframe, 'Inserir Aluno', 2, 2, (W,E),
               self.__set_insert_students_screen)
        button(self.__mainframe, 'Visualizar Professores', 2, 3, (W,E),
               self.__set_teachers_table_screen)
        button(self.__mainframe, 'Visualizar Alunos', 2, 4, (W,E),
               self.__set_students_table_screen)
        label(self.__mainframe, 2, 5, (W,E))
        button(self.__mainframe, 'Sair', 2, 6, (W,E), exit)
    
    def __set_insert_teacher_screen(self) -> None:
        InsertTeacherScreen(self.__root)
            
    def __set_insert_students_screen(self) -> None:
        InsertStudentScreen(self.__root)
        
    def __set_teachers_table_screen(self) -> None:
        TeachersTableScreen(self.__root)

    def __set_students_table_screen(self) -> None:
        StudentsTableScreen(self.__root)
        
UserInterface()