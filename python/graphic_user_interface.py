from tkinter import Tk, ttk
from tkinter import *
from insert_teacher_screen import InsertTeacherScreen
from insert_student_screen import InsertStudentScreen
from students_table_screen import StudentsTableScreen
from teachers_table_screen import TeachersTableScreen
from edit_student_screen import EditStudentScreen
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
        
        text_and_commands = (
            ('Inserir Professor', self.__set_insert_teacher_screen),
            ('Inserir Aluno', self.__set_insert_students_screen),
            ('Pesquisar Aluno', self.__set_edit_student_screen),
            ('Visualizar Professores', self.__set_teachers_table_screen),
            ('Visualizar Alunos', self.__set_students_table_screen),
        )
        
        label(self.__mainframe, 1, 1, (W,E))
        label(self.__mainframe, 3, 1, (W,E))
        row = 1
        
        for text, command in text_and_commands:
            button(self.__mainframe, text, 2, row, (W,E), command)
            row += 1
        
        label(self.__mainframe, 2, row, (W,E))
        button(self.__mainframe, 'Sair', 2, row + 1, (W,E), exit)
    
    def __set_insert_teacher_screen(self) -> None:
        InsertTeacherScreen(self.__root)
            
    def __set_insert_students_screen(self) -> None:
        InsertStudentScreen(self.__root)
        
    def __set_edit_student_screen(self) -> None:
        EditStudentScreen(self.__root)
        
    def __set_teachers_table_screen(self) -> None:
        TeachersTableScreen(self.__root)

    def __set_students_table_screen(self) -> None:
        StudentsTableScreen(self.__root)
        
UserInterface()