from tkinter import Tk, ttk
from tkinter import *
from insert_teacher_screen import InsertTeacherScreen
from insert_student_screen import InsertStudentScreen
from screen import Screen

class UserInterface(Screen):
    
    def __init__(self) -> None:
        self.window = Tk()
        self.mainframe = ttk.Frame(self.window, padding='5')
        self.__set_all_buttons()
        
        self.configure_screen('Escola Edutech')
        self.window.mainloop()
        
    def __set_all_buttons(self) -> None:
        ttk.Button(self.mainframe, 
                   text='Inserir Professor', 
                   command=self.__set_insert_teacher_screen).grid(column=2, 
                                                                  row=1, 
                                                                  sticky=(W,E))
        ttk.Button(self.mainframe, 
                   text='Inserir Aluno', 
                   command=self.__set_insert_students_screen).grid(column=2, 
                                                                   row=2, 
                                                                   sticky=(W,E))
        ttk.Button(self.mainframe, 
                   text='Visualizar Professores',
                   command=self.__set_teachers_table_screen).grid(
                                                    column=2, row=3, 
                                                       sticky=(W,E))
        ttk.Button(self.mainframe, 
                   text='Visualizar Alunos',
                   command=self.__set_students_table_screen).grid(
                                                    column=2, row=4,
                                                  sticky=(W,E))
        ttk.Label(self.mainframe).grid(column=2, row=5, sticky=(W,E))
        ttk.Button(self.mainframe, text='Sair', command=exit).grid(column=2, 
                                                                     row=6, 
                                                                     sticky=(W,E))
    
    def __set_insert_teacher_screen(self) -> None:
        InsertTeacherScreen(self.window)
            
    def __set_insert_students_screen(self) -> None:
        InsertStudentScreen(self.window)
        
    def __set_teachers_table_screen(self) -> None:
        pass

    def __set_students_table_screen(self) -> None:
        pass        
        
UserInterface()