from tkinter import *
from tkinter import StringVar, Toplevel, ttk, messagebox
from screen import Screen
from instructor import Instructor
from errors import (InvalidNameError, InvalidEmailError, 
                    InvalidClassesError, InvalidShiftError)

class InsertTeacherScreen(Screen):
    
    def __init__(self, root) -> None:
        
        self.window = Toplevel(root)
        self.mainframe = ttk.Frame(self.window, padding='5')
        self.__name = StringVar()
        self.__email = StringVar()
        self.__classes = StringVar()
        self.__shift = StringVar()
        self.__data = [self.__name, self.__email, self.__classes,
                       self.__shift]
        
        self.__set_buttons()
        self.__set_labels()
        self.__set_entries()
        self.configure_screen('Inserir Professor')
        
    def __set_buttons(self) -> None:
        
        ttk.Button(self.mainframe, 
                   text='Cancelar', 
                   command=self.window.destroy).grid(column=5, row=6,
                                                       sticky=(W,E))
        ttk.Button(self.mainframe,
                   text='Criar Professor',
                   command=self.__try_to_create_teacher).grid(column=6,
                                                              row=6,
                                                              sticky=(W,E))
                   
    def __set_labels(self) -> None:
        
        ttk.Label(self.mainframe, text='Nome: ').grid(column=1, 
                                                        row=1)
        ttk.Label(self.mainframe, text='E-mail: ').grid(column=3, 
                                                          row=1)
        ttk.Label(self.mainframe, text='Turmas (separe as turmas por vírgulas): ').grid(
                  column=5, row=1)
        
        ttk.Label(self.mainframe, text='Turno: ').grid(column=1, 
                                                       row=2)
        
    def __set_entries(self) -> None:
        
        ttk.Entry(self.mainframe, textvariable=self.__name).grid(
            column=2, row=1)
        ttk.Entry(self.mainframe, textvariable=self.__email).grid(
            column=4, row=1)
        ttk.Entry(self.mainframe, textvariable=self.__classes).grid(
            column=6, row=1)
        
        ttk.Radiobutton(self.mainframe, variable=self.__shift,
                  text='Manhã', value='M').grid(column=2, row=2, 
                                            sticky=W)
        ttk.Radiobutton(self.mainframe, variable=self.__shift,
                  text='Tarde', value='T').grid(column=3, row=2, 
                                            sticky=W)
    
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
                self.window.destroy()
        
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