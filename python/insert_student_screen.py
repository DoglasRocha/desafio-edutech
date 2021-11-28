from tkinter import *
from tkinter import ttk, messagebox
from errors import (InvalidNameError, InvalidEmailError, InvalidClassError,
                    InvalidCGMError, InvalidStatusError, InvalidShiftError, 
                    InvalidTeacherNameError)
from assets import button, radio_button, label, entry
from student import Student
from screen import Screen

class InsertStudentScreen(Screen):
    
    def __init__(self, root) -> None:
        
        self.__window = Toplevel(root)
        self.__mainframe = ttk.Frame(self.__window, padding='5')
        self.__name = StringVar()
        self.__email = StringVar()
        self.__class = StringVar()
        self.__CGM = StringVar()
        self.__shift = StringVar()
        self.__status = StringVar()
        self.__teacher = StringVar()
        self.__data = [self.__name, self.__email, self.__class, 
                       self.__CGM, self.__shift, self.__status,
                       self.__teacher]
        
        self.__set_buttons()
        self.__set_labels()
        self.__set_entries()
        Screen.configure_screen('Inserir Aluno', self.__window, 
                                self.__mainframe)
    
    def __set_buttons(self) -> None:
        
        button(self.__mainframe, 'Cancelar', 5, 6, (W,E), (self.__window
                                                         .destroy))
        
        button(self.__mainframe, 'Criar Aluno', 6, 6, (W,E), (self
                                            .__try_to_create_student))
                   
    def __set_labels(self) -> None:
        
        label(self.__mainframe, 1, 1, text='Nome:')
        label(self.__mainframe, 3, 1, text='E-mail:')
        label(self.__mainframe, 5, 1, text='Turma:')
        
        label(self.__mainframe, 1, 2, text='CGM:')
        label(self.__mainframe, 3, 2, text='Turno:')
        
        label(self.__mainframe, 1, 1, text='Professor:')
        label(self.__mainframe, 1, 1, text='Status:')
            
    def __set_entries(self) -> None:
        
        ttk.Entry(self.__mainframe, textvariable=self.__name).grid(
            column=2, row=1)
        ttk.Entry(self.__mainframe, textvariable=self.__email).grid(
            column=4, row=1)
        ttk.Entry(self.__mainframe, textvariable=self.__class).grid(
            column=6, row=1)
        
        ttk.Entry(self.__mainframe, textvariable=self.__CGM).grid(
            column=2, row=2)
        ttk.Radiobutton(self.__mainframe, variable=self.__shift,
                  text='Manhã', value='M').grid(column=4, row=2, 
                                            sticky=W)
        ttk.Radiobutton(self.__mainframe, variable=self.__shift,
                  text='Tarde', value='T').grid(column=5, row=2, 
                                            sticky=W)
        
        ttk.Entry(self.__mainframe, textvariable=self.__teacher).grid(
            column=2, row=3)            
        ttk.Radiobutton(self.__mainframe, variable=self.__status,
                        text='Ativo', value='ATIVO').grid(
            column=4, row=3, sticky=W)
        ttk.Radiobutton(self.__mainframe, variable=self.__status,
                        text='Inativo', value='INATIVO').grid(
            column=5, row=3, sticky=W)      
            
    def __try_to_create_student(self) -> None:
        
        for data in self.__data:
            if '' == data.get():
                (messagebox.
                showwarning('Entrada inválida', 
                            message='Todos os campos devem ser preenchidos!!'))
                break
            
        try:
            student = Student(self.__name.get(), self.__email.get(), 
                              self.__class.get(), self.__CGM.get(),
                              self.__shift.get(), self.__status.get(), 
                              self.__teacher.get())
            message = ('Você tem certeza que quer cadastrar esse aluno?\n'
                       + f'Nome: {self.__name.get()}, Email: {self.__email.get()}\n'
                       + f'Turma: {self.__class.get()}, CGM: {self.__CGM.get()}\n'
                       + f'Status: {self.__status.get()}, Turno: {self.__shift.get()}\n'
                       + f'Nome do professor: {self.__teacher.get()}')
            
            if messagebox.askyesno('Tem certeza?', message=message):
                student.send_to_database()
                self.__window.destroy()
        
        except InvalidNameError:
            messagebox.showwarning('Nome Inválido',
                                   message='O nome preenchido é inválido!!')
            
        except InvalidEmailError:
            messagebox.showwarning('Email Inválido',
                                   message='O email preenchido é inválido!!')
        
        except InvalidClassError:
            messagebox.showwarning('Turma Inválida',
                                   message='A turma preenchida é inválida!!')
        
        except InvalidCGMError:
            messagebox.showwarning('CGM Inválido',
                                   message='O CGM preenchido é inválido!!')
        
        except InvalidStatusError:
            messagebox.showwarning('Status Inválido',
                                   message='O status preenchido é inválido!!')
        
        except InvalidShiftError:
            messagebox.showwarning('Turno Inválido',
                                   message='O turno preenchido é inválido!!')
        
        except InvalidTeacherNameError:
            message = ('O nome do professor informado é inválido. Caso nenhum' +
            ' professor tenha sido cadastrado, é necessário cadastrar um professor!!')
            
            messagebox.showwarning('Nome Inválido',
                                   message=message)
    
