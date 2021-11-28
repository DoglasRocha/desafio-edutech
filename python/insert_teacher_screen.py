from tkinter import *
from tkinter import StringVar, Toplevel, ttk, messagebox
from screen import Screen
from instructor import Instructor
from assets import button, label, entry, radio_button
from errors import (InvalidNameError, InvalidEmailError, 
                    InvalidClassesError, InvalidShiftError)

class InsertTeacherScreen(Screen):
    
    def __init__(self, root) -> None:
        
        self.__window = Toplevel(root)
        self.__mainframe = ttk.Frame(self.__window, padding='5')
        self.__name = StringVar()
        self.__email = StringVar()
        self.__classes = StringVar()
        self.__shift = StringVar()
        self.__data = [self.__name, self.__email, self.__classes,
                       self.__shift]
        
        self.__set_buttons()
        self.__set_labels()
        self.__set_entries()
        Screen.configure_screen('Inserir Professor', self.__window, 
                                self.__mainframe)
        
    def __set_buttons(self) -> None:
        
        button(self.__mainframe, 'Cancelar', 5, 6, (W,E), (self.__window
                                                         .destroy))
        
        button(self.__mainframe, 'Criar Professor', 6, 6, (W,E), (self
                                            .__try_to_create_teacher))
                   
    def __set_labels(self) -> None:
        
        label(self.__mainframe, 1, 1, text='Nome:')
        label(self.__mainframe, 3, 1, text='E-mail:')
        label(self.__mainframe, 5, 1, text='Turmas (separe as turmas'
              + 'por vírgula):')
        label(self.__mainframe, 1, 2, text='Turno:')
        
    def __set_entries(self) -> None:
        
        entry(self.__mainframe, self.__name, 2, 1)
        entry(self.__mainframe, self.__email, 4, 1)
        entry(self.__mainframe, self.__classes, 6, 1)
        
        radio_button(self.__mainframe, self.__shift, 'Manhã', 'M', 2, 
                     2, (W))
        radio_button(self.__mainframe, self.__shift, 'Tarde', 'T', 3, 
                     2, (W))
    
    def __try_to_create_teacher(self) -> None:
        
        for data in self.__data:
            if '' == data.get():
                (messagebox.
                showwarning('Entrada inválida', 
                            message='Todos os campos devem ser preenchidos!!'))
                break
            
        try:
            instructor = Instructor(self.__name.get(), self.__email.get(), self.__classes.get(),
                       self.__shift.get())
            
            message = ('Você tem certeza que quer cadastrar esse professor?\n'
                       + f'Nome: {self.__name.get()}, Email: {self.__email.get()}\n'
                       + f'Turmas: {self.__classes.get()}, Turno: {self.__shift.get()}')
            
            if messagebox.askyesno('Tem certeza?', message=message):
                instructor.send_to_database()
                self.__window.destroy()
        
        except InvalidNameError:
            messagebox.showwarning('Nome Inválido',
                                   message='O nome preenchido é inválido!!')
            
        except InvalidEmailError:
            messagebox.showwarning('Email Inválido',
                                   message='O email preenchido é inválido!!')
        
        except InvalidClassesError:
            messagebox.showwarning('Turma Inválida',
                                   message='A turma preenchida é inválida!!')
            
        except InvalidShiftError:
            messagebox.showwarning('Turno Inválido',
                                   message='O turno preenchido é inválido!!')