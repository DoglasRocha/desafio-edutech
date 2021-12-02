from tkinter import *
from tkinter import ttk
from assets import button, radio_button, label, entry
from student_validator import StudentValidator
from screen import Screen

class InsertStudentScreen(Screen, StudentValidator):
    
    def __init__(self, root: Tk) -> None:
        
        self._window = Toplevel(root)
        self.__mainframe = ttk.Frame(self._window, padding='5')
        self._name = StringVar()
        self._email = StringVar()
        self._class = StringVar()
        self._CGM = StringVar()
        self._shift = StringVar()
        self._status = StringVar()
        self._teacher = StringVar()
        self._data = [self._name, self._email, self._class, 
                       self._CGM, self._shift, self._status,
                       self._teacher]
        
        self.__set_buttons()
        self.__set_labels()
        self.__set_entries()
        self.configure_screen('Inserir Aluno', self._window, 
                                self.__mainframe)
    
    def __set_buttons(self) -> None:
        
        button(self.__mainframe, 'Cancelar', 5, 6, (W,E), (self._window
                                                         .destroy))
        
        button(self.__mainframe, 'Criar Aluno', 6, 6, (W,E), (self
                                            .try_to_create_student))
                   
    def __set_labels(self) -> None:
        
        label(self.__mainframe, 1, 1, text='Nome:')
        label(self.__mainframe, 3, 1, text='E-mail:')
        label(self.__mainframe, 5, 1, text='Turma:')
        
        label(self.__mainframe, 1, 2, text='CGM:')
        label(self.__mainframe, 3, 2, text='Turno:')
        
        label(self.__mainframe, 1, 3, text='Professor:')
        label(self.__mainframe, 3, 3, text='Status:')
            
    def __set_entries(self) -> None:
        
        entry(self.__mainframe, self._name, 2, 1)
        entry(self.__mainframe, self._email, 4, 1)
        entry(self.__mainframe, self._class, 6, 1)
        
        entry(self.__mainframe, self._CGM, 2, 2)
        radio_button(self.__mainframe, self._shift, 'Manhã', 'M',
                     4, 2, (W))
        radio_button(self.__mainframe, self._shift, 'Tarde', 'T',
                     5, 2, (W))
        
        entry(self.__mainframe, self._teacher, 2, 3)     
        radio_button(self.__mainframe, self._status, 'Ativo', 
                     'ATIVO', 4, 3, (W))
        radio_button(self.__mainframe, self._status, 'Inativo', 
                     'INATIVO', 5, 3, (W))  
    
