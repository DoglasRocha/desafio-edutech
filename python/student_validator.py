from tkinter import messagebox
from student import Student
from errors import (ExistentStudentError, InvalidNameError, InvalidEmailError, 
                    InvalidClassError, InvalidCGMError,
                    InvalidShiftError, InvalidStatusError,
                    InvalidTeacherNameError)

class StudentValidator:
    
    def try_to_create_student(self, create_student: bool=True) -> None:
        
        word = 'cadastrar' if create_student else 'atualizar'
        
        for data in self._data:
            if '' == data.get():
                (messagebox.
                showwarning(
                    'Entrada inválida', 
                    message='Todos os campos devem ser preenchidos!!'))
                break
            
        try:
            student = Student(self._name.get(), self._email.get(), 
                              self._class.get(), self._CGM.get(),
                              self._shift.get(), self._status.get(), 
                              self._teacher.get())
            message = (f'Você tem certeza que quer {word} esse aluno?\n'
                       + f'Nome: {self._name.get()}\n'
                       + f'Email: {self._email.get()}\n'
                       + f'Turma: {self._class.get()}\n' 
                       + f'CGM: {self._CGM.get()}\n'
                       + f'Status: {self._status.get()}\n'
                       + f'Turno: {self._shift.get()}\n'
                       + f'Nome do professor: {self._teacher.get()}')
            
            if messagebox.askyesno('Tem certeza?', message=message):
                if create_student:
                    student.insert_into_database()
                else:
                    student.update_student()
                    
                self._window.destroy()
        
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
            
        except ExistentStudentError:
            
            messagebox.showwarning('Nome Inválido',
                                   message='Esse aluno já foi cadastrado!!')